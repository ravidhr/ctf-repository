from z3 import *

def isarousing(x):
    i = x % 10
    print(i)
    #i = 9
    x /= 10

    j = x % 10
    print(j)
    #j = 6
    x /= 10

    if j % 2 != 0:
        return False

    if i != j / 2 * 3:
        return False


    for k in range(3):
        if x % 10 != i:
            return False
        x /= 10
        if x % 10 != j:
            return False
        x /= 10

    if x != 0:
        return False
    else:
        return True

    if i % 2 == 0:
        return False

    if i ^ j == 15:
        return True
    else:
        return False

def main():
    # happy number
    i = 270719 * 6317
    print(i)
    # j
    for j in range(9999):
        if (j & 0xff == 0) and (j >> 12 == 0) and (j >> 8 ^ 0xf) == 4:
            print(j)
            break
    # k
    k = 19800828
    print(k)
    # m
    #m = Int('m')
    m = Int('m')
    s = Solver()

    #i = m % 10
    i = 9
    m /= 10

    #j = m % 10
    j = 6
    m /= 10

    #s.add(i == j/2*3)

    for a in range(3):
        s.add(m % 10 == i)
        m /= 10
        s.add(m % 10 == j)
        m /= 10

    s.add(m == 0)
    #s.add(i % 2 != 0)
    #s.add((i ^ j) == 15)

    if s.check() == sat:
        res = s.model()
        print(res)
    else:
        print("nope :(")

    #for a in range(10):
    #    for b in range(10):
    #        if a % 2 == 0 and b % 2 != 0 and a ^ b == 15 and a == b / 2 * 3:
    #            print("a = {}".format(a))
    #            print("b = {}".format(b))
    #        if a % 2 != 0 and b % 2 == 0 and a ^ b == 15 and b == a / 2 * 3:
    #            print("a = {}".format(a))
    #            print("b = {}".format(b))

    # i di arousing 9
    # j di arousing 15

    print(isarousing(69696900))

    #for i in range(9999):
    #    if isarousing(i) == True:
            #print("ketemu : {}".format(i))
            #print("apa")
    #        print("ketemu : {}".format(i))


if __name__ == "__main__":
    main()
