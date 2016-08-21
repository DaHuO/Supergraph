import sys

def g(x):
    c = [0] * 10
    z = x
    while True:
        y = z
        while y > 0:
            c[y % 10] = 1
            y //= 10
        if sum(c) >= 10:
            break
        z += x
    return z

l = sys.stdin.readline()
m = int(l.strip())

for i in range(0, m):
    l = sys.stdin.readline()
    n = int(l.strip())
    if n == 0:
        print("Case #%d: INSOMNIA" % (i + 1))
    else:
        print("Case #%d: %d" % (i + 1, g(n)))

