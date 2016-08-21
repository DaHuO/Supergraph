__author__ = 'rutger'


def setDigits(n, d):
    y = n
    while y:
        mod = y % 10
        y //= 10
        d[mod] = True
    return d


def allDigits(d):
    for i in range(len(d)):
        if not d[i]:
            return False
    return True


def f(n):
    if n == 0:
        return "INSOMNIA"

    y = n
    digits = [False] * 10
    for i in range(1000):
        digits = setDigits(y, digits)
        if allDigits(digits):
            return y
        y += n
    return "INSOMNIA"


T = int(input())
for t in range(T):
    x = int(input())
    result = str(f(x))
    print("Case #%d: %s" % (t + 1, result))