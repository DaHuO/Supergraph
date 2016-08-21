import random
a = {}
def isComplex(x):
    if x == 1:
        return 0
    i = 2
    while i <= 1000:
        if x % i == 0:
            return i
        i += 1
    return 0
while len(a) < 500:
    n = 31
    x = (1 << n) + random.randint(0, (1 << (n - 1)) - 1) * 2 + 1
    good = True
    v = []
    for s in range(2, 11):
        t = x
        p = 0
        for i in range(n + 1):
            p *= s
            if t % 2 == 1:
                p += 1
            t //= 2
        res = isComplex(p)
        if not res:
            good = False
            break
        v.append(res)
        pass
    if good:
        a[x] = v
for p in a:
    s = bin(p)[2:][::-1]
    s += " "
    for x in a[p]:
        s += str(x) + " "
    print(s)



