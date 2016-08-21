import sys


def digits(n):

    res = []
    while n > 0:
        res.append(n % 10)
        n = n / 10

    return res


T = int(sys.stdin.next())

for i in range(T):
    n = int(sys.stdin.next())
    if n == 0:
        print('Case #%i: INSOMNIA' % (i + 1,))
    else:
        s = set(digits(n))
        y = 1
        while len(s) < 10:
            y += 1
            s = s.union(set(digits(y * n)))
        print('Case #%i: %i' % (i + 1, y * n))
