def printsol(i, n):
    print("Case #" + str(i) + ": " + str(n))

def f(i, s):
    r = 0
    for k in range(0, len(s) - 1):
        if s[k] != s[k + 1]:
            r += 1
    if s[-1] == '-':
        r += 1
    printsol(i, r)

with open("bl.in") as fin:
    n = int(fin.readline())
    for i in range(n):
        f(i + 1, fin.readline()[:-1])
