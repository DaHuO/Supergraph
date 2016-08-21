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

def solve(n):
    if n == 0: return "INSOMNIA"
    nums = set(list(str(n)))
    cur = n
    while len(nums) < 10:
        cur += n
        for c in str(cur):
            nums.add(c)
    return cur


T = ri()
result = []
for x in xrange(T):
    n = ri()
    result.append("Case #%s: %s"%(x+1, solve(n)))
with open("./ares", "w+") as f:
    f.write("\n".join(result))
