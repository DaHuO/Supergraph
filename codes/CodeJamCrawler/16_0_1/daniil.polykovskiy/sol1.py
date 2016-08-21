import sys

def sol(N):
    if N == 0:
        return "INSOMNIA"
    s = set()
    for i in range(1, 200):
        s |= set(str(N*i))
        if len(s) == 10:
            return N*i

inp = open(sys.argv[1])
out = open(sys.argv[2], 'w')
T = int(inp.readline())
for i in range(T):
    N = int(inp.readline())
    out.write("Case #{}: {}\n".format(i+1, sol(N)))
inp.close()
out.close()