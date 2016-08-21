import sys
import itertools

def g(s):
    l = len(s)
    divisors = []
    for i in range(2, 11):
        found = False
        for d in r.keys():
            remainder = sum([r[d][i][l-k-1] if s[k] == '1' else 0 for k in range(0, l)]) % d
            if remainder == 0:
                found = True
                divisors.append(d)
                break
        if not found:
            return None
    return divisors

# Fill remainder table

r = {}

for d in (2, 3, 5, 7, 11, 13):
    r[d] = {}
    for i in range(2, 11):
        r[d][i] = []
        for k in range(0, 32):
            if k == 0:
                r[d][i].append(1)
            else:
                r[d][i].append((r[d][i][k-1] * i) % d)

l = sys.stdin.readline()
m = int(l.strip())

for i in range(0, m):
    l = sys.stdin.readline()
    tokens = l.strip().split(" ")
    n = int(tokens[0])
    j = int(tokens[1])
    res = []
    for middle in map(''.join, itertools.product("01", repeat=n-2)):
        s = "%d%s%d" % (1, middle, 1)
        divisors = g(s)
        if divisors is not None:
            res.append((s, divisors))
        if len(res) >= j:
            break
    print("Case #%d:" % (i + 1))
    for (s, divisors) in res:
        print("%s %s" % (s, " ".join([str(d) for d in divisors])))

