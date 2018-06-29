
def main():
    plain = "Here is a sample. Pay close attention!"
    cipher = "2e0c010d46000048074900090b191f0d484923091f491004091a1648071d070d081d1a070848".decode("hex")

    key = ""

    for i in range(len(plain)):
        key += chr(ord(plain[i]) ^ ord(cipher[i]))

    flag_cipher = "0005120f1d111c1a3900003712011637080c0437070c0015".decode("hex")

    flag = ""
    for i in range(len(flag_cipher)):
        flag += chr(ord(flag_cipher[i]) ^ ord(key[i]))

    print(flag)


if __name__ == "__main__":
    main()
