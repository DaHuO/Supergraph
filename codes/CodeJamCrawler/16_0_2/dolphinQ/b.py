import sys, math
def rs():
    return sys.stdin.readline().strip()
def ri():
    return int(sys.stdin.readline().strip())
def ras():
    return list(sys.stdin.readline().strip())
def rai():
    return map(int,sys.stdin.readline().strip().split())
def raf():
    return map(float,sys.stdin.readline().strip().split())

def solve(st):
    res = 0
    l = len(st)
    if l == 0: return 0
    cur = st[0]
    for i in xrange(1, l):
        v = st[i]
        if cur != v:
            res += 1
            cur = v
    if cur == "-":
        return res + 1
    else:
        return res


T = ri()
result = []
for x in xrange(T):
    inp = ras()
    result.append("Case #%s: %s"%(x+1, solve(inp)))
with open("./res", "w+") as f:
    f.write("\n".join(result))
