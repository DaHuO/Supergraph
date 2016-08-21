outf = open("output.txt", "w")
inf = open("input.txt", "r")
t = int(inf.readline())
n, j = map(int, inf.readline().split())
res = 0
print("Case #1:", file=outf)

def getdiv(a):
    for i in range(2, a + 1):
        if (a % i == 0):
            return i;
        if (i * i > a):
            return a;
        
for i in range(1 << (n - 2)):
    rs = '1' + '0' * (n - 2 - len(str(bin(i))[2:])) + str(bin(i))[2:] + '1'
    q = True
    for d in range(2, 11):
        val = int(rs, d)
        if (getdiv(val) == val):
            q = False;
    if (q):
        print(rs, end=' ', file=outf)
        for d in range(2, 11):
            val = int(rs, d)
            print(getdiv(val), end=' ', file=outf)
        print(file=outf)
        res += 1
        if (res == j):
            break
outf.close()
