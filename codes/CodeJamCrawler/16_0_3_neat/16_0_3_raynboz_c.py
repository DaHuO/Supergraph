fin = open("cin.txt", "r")
fout = open("cout.txt", "w")

N = 16
J = 50

def conv(x, base):
    n = 0
    a = 0
    while x > 0:
        if x % 2 == 1:
            n += base**a
        x = x // 2
        a += 1
    return n


def notPrime(x):
    if x % 3 == 0:
        return 3
    i = 5
    w = 2
    while i * i <= x:
        if x % i == 0:
            return i
        i += w
        w = 6 - w
    return 0

def solve():
    s = 2**(N-1) + 1
    count = 0

    for i in range(2**(N-2)):
        proof = []
        works = True
        for j in range(2, 11):
            proof += [notPrime(conv(s + 2*i, j))]
            if proof[-1] == 0:
                works = False
                break
        if works:
            count += 1
            fout.write(str(bin(s+2*i))[2:])
            for p in proof:
                fout.write(" " + str(p))
            fout.write("\n")
            #print(str(bin(s+2*i))[2:], proof)
            if count >= J:
                break
    return s

for i in range(1):
    fout.write("Case #1:\n")
    solve()

fin.close()
fout.close()
