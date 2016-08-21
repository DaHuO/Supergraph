import sys

def g(k, s):
    res = []
    l = k
    while l > 2 and s >= 0:
        res.append((k - l) * k + (k - l + 2))
        s -= 1
        if s <= 0:
            break
        l -= 2
    if l > 2:
        return None
    res.append((k - l) * k + k)
    return res

l = sys.stdin.readline()
m = int(l.strip())

for i in range(0, m):
    l = sys.stdin.readline()
    tokens = l.strip().split(" ")
    k = int(tokens[0])
    c = int(tokens[1])
    s = int(tokens[2])
    if c == 1:
        if s < k:
            print("Case #%d: IMPOSSIBLE" % (i + 1))
        else:
            print("Case #%d: %s" % (i + 1, " ".join([str(j + 1) for j in range(0, k)])))
    else:
        res = g(k, s)
        if res is None:
            print("Case #%d: IMPOSSIBLE" % (i + 1))
        else:
            print("Case #%d: %s" % (i + 1, " ".join([str(v) for v in res])))

