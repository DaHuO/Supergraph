def listnum(n):
    l = set([])
    while n > 0:
        l.add(n % 10)
        n //= 10
    return l

def printsol(i, n):
    print("Case #" + str(i) + ": " + str(n))

def f(i, n):
    if n == 0:
        printsol(i, "INSOMNIA")
    else:
        current = 0
        s = set([])
        while [i for i in range(10) if i not in s] != []:
            current += n
            s = s.union(listnum(current))
        printsol(i, current)

with open("al.in") as fin:
    n = int(fin.readline())
    for i in range(n):
        f(i + 1, int(fin.readline()))
