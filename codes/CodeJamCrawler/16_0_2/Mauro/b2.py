from toolz import *

def read_int():
    return int(raw_input())

def solve(x):
    r = list(map(first, partitionby(identity, x)))
    return len(r) if x[-1]=='-' else len(r)-1
    
for case in range(read_int()):
    S = raw_input()
    ans = solve(S)
    print "Case #%d: %s" % (case+1, ans)
