import sys

def get(k, c, pos):
    return 1 + k**(c-1)*pos

def solve(testcase):
    k,c,s = map(int, sys.stdin.readline().strip().split())
    print "Case #%d:" % testcase,
    assert k == s
    print " ".join([str(get(k,c,i)) for i in range(s)])
for t in range(int(sys.stdin.readline().strip())):
    solve(t+1)
