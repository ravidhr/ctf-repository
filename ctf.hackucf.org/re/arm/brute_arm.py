
def main():
    flag_enc = "huL{SEp^H6?!"

    # generate key
    key = []
    for i in range(255):
        res = ""
        for j in range(len(flag_enc)):
            res += chr((7 * j + i) % 126)
        key.append(res)
        res = ""

    # brute flag
    for i in range(255):
        flag = ""
        for j in range(len(flag_enc)):
            flag += chr(ord(flag_enc[j]) ^ ord(key[i][j]))
        print(flag)
        flag = ""

if __name__ == "__main__":
    main()
