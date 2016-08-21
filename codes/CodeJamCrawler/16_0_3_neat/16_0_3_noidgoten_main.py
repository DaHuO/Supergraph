N = 32
J = 500

res = []

a = int(N / 2) - 1


def decompose(n, a):
    r = [1]
    while n:
        r.append(n & 1)
        n = int(n / 2)
    for i in range(a + 1 - len(r)):
        r.append(0)
    r.append(1)
    return r


def numberify1(l):
    pow = 1
    r = 0
    for i in range(N):
        if i in l:
            r += pow
        pow *= 10
    return r


def numberify2(l, base):
    pow = 1
    r = 0
    for i in l:
        r += i * pow
        pow *= base
    return r

while len(res) < J and a >= 2:
    for i in range(2 ** (a - 2)):
        l1 = decompose(i, a - 2)
        for j in range(2 ** (N - a - 1)):
            l2 = decompose(j, N - a - 1)
            ok = True
            test = []
            x = 0
            while ok and x < len(l1):
                y = 0
                while ok and y < len(l2):
                    if l1[x] and l2[y] and (x + y) not in test:
                        test.append(x + y)
                    elif l1[x] and l2[y] and (x + y) in test:
                        ok = False
                    y += 1
                x += 1
            if ok:
                res.append([test, l1])
                if len(res) == J:
                    f = open('main.out', 'w')
                    f.write('Case #1:\n')
                    for r in res:
                        f.write(str(numberify1(r[0])) + ' ')
                        for base in range(2, 11):
                            f.write(str(numberify2(r[1], base)) + ' ')
                        f.write('\n')
                    exit(0)
    a -= 1

