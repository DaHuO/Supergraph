import sys
from itertools import groupby

T = int(input())

def solve(t, pile):
    groups = len(["".join(group) for _, group in groupby(pile)])
    res = groups
    if pile[-1] == "+":
        res -= 1
    print("Case #%d: %d" %(t,res))

for t, line in enumerate(sys.stdin):
    solve(t+1, line.strip())
