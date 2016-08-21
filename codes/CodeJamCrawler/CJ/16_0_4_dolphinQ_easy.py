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

def solve():
    K, C, S = rai()
    return " ".join(map(str,range(1,K+1)))


T = ri()
result = []
for x in xrange(T):
    result.append("Case #%s: %s"%(x+1, solve()))
with open("./res", "w+") as f:
    f.write("\n".join(result))
