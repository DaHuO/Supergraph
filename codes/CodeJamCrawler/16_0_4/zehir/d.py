def printsolution(i, s):
    print("Case #" + str(i) + ": " + str(s))

def f(n, k, c, s):
    l = []
    mintile = k // c + (1 if k % c != 0 else 0)
    if s < mintile:
        printsolution(n, "IMPOSSIBLE")
    else:
        for i in range(mintile):
            r = 0
            for j in range(c if k > (i + 1) * c else k - i * c):
                r += (i * c + j) * pow(k, c - 1 - j)
            l.append(r)
        printsolution(n, ' '.join([str(t + 1) for t in l]))

with open("dl.in") as fin:
    n = int(fin.readline())
    for i in range(n):
        k, c, s = fin.readline().split(' ')
        f(i + 1, int(k), int(c), int(s))
