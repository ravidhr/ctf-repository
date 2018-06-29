from pwn import *

def main():
    r = remote("ctf.hackucf.org",10101)
    r.recvuntil("Better be quick, you only have 30 seconds!\n")

    for i in range(100):
        try:
            r.recvuntil("Value: ")
            value = r.recvline().strip()
            r.sendline(value)
        except:
            r.interactive()

    r.interactive()



if __name__ == "__main__":
    main()
