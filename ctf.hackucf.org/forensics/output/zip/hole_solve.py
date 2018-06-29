
def main():
    f = open("data.txt","rb").read()[:-1].split("\n")
    data_hex = ""
    for line in f:
        res = line.split(" ")
        num = 1
        while num <= 8:
            if res[num] != "":
                data_hex += res[num].decode("hex")
            num += 1
        num = 1


    open("res","wb").write(data_hex)

if __name__ == "__main__":
    main()
