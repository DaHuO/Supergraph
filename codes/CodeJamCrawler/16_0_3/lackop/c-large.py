import math
N = 500

def getdiv(n):
    #print(n)
    for i in range(2, 1000):#math.floor(math.sqrt(n))):
        if n % i == 0:
            return i

    return - 1

pocet = 0

with open('c-large.txt', 'w') as fout:
    fout.write("Case #1:\n")

#for i in range(int("1000000000000001", 2), int("1111111111111111", 2) + 1, 2):
for i in range(int("10000000000000000000000000000001", 2), int("11111111111111111111111111111111", 2) + 1, 2):
#for i in range(int("100001", 2), int("1111111", 2) + 1, 2):
    #print(i)
    out = [bin(i)[2:]]
    for base in range(2, 11):
        #r = (int(baseN(int(bin(i)[2:], 10), base)))
        r = getdiv(int(bin(i)[2:], base))
        if r != -1:
            out.append(r)
        else:
            break

    #print(out)
    if len(out) == 10:
        print(pocet, out)
        pocet += 1

        with open('c-large.txt', 'a') as fout:
            fout.write(" ".join(map(str, out)) + "\n")

        #numersfound.append(i)
        if pocet == N:
            exit()
