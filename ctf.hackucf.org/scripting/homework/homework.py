from pwn import *

def main():
    r = remote("ctf.hackucf.org",10104)
    r.recvuntil("If you complete it for me, I'll give you a flag in return!\n")

    j = 1
    while True:
        try:
            data = r.recvuntil("=")[:-1]
            answer = eval(data)
            print(data)
            print(answer)
            print(j)
            r.sendline(answer)
            j += 1
        except:
            r.interactive()
            break

    #r.interactive()
if __name__ == "__main__":
    main()
