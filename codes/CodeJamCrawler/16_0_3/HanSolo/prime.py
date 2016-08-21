import math
__author__ = 'vladimir'


def divisor(n):
    for i in range(2, int(math.sqrt(n) + 1) + 1):
        if n % i == 0:
            return i
    return -1

if __name__ == "__main__":
    inp = open("C-small-attempt0.in")
    output = open("output.txt", 'w+')
    inp.readline()

    NJ = inp.readline().strip().split(" ")
    N = int(NJ[0])
    J = int(NJ[1])
    output.write("Case #1:\n")
    a = 3
    total = 0
    while total < J:
        while a & 1 == 0:
            a += 1
        bi = "{0:b}".format(a)
        if len(bi) == N:
            candidate = True
            delim = []
            delim.append(bi)

            for j in range(2, 11):
                if candidate:
                    cur = int(bi, j)
                    d = divisor(cur)
                    if d == -1:
                        candidate = False
                    else:
                        delim.append(str(d))

            if candidate:
                print(" ".join(delim))
                output.write(" ".join(delim) + "\n")
                total += 1
        elif len(bi) > N:
            break

        a += 1
    inp.close()
    output.close()
