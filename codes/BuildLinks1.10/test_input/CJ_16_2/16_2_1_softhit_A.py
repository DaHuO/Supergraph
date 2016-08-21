#!python3
import sys
import math
from functools import reduce

from operator import xor
# tfile = sys.stdin
from collections import deque, defaultdict,Counter
read = lambda fd=sys.stdin, t=int: t(fd.readline())
readlist = lambda fd=sys.stdin, t=int: list(map(t, fd.readline().split()))
readtuple = lambda fd=sys.stdin, t=int: tuple(map(t, fd.readline().split()))

# ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")

def solve(t,s):
    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    digmap = { i:digits[i] for i in range(10)}
    # print(digmap)
    # uniq numb: 8: eight
    scnt = Counter(S.strip())
    cnt = Counter()
    for d in digits:
        for a in d:
            cnt[a] += 1
    # print(cnt)
    ret = []
    while sum(scnt.values()) >0:
        if scnt['U'] > 0:
            for i in range(scnt['U']):
                ret.append(4)
                scnt.subtract(digmap[4])
            # reduce 4
        if scnt['G'] > 0:
            for i in range(scnt['G']):
                ret.append(8)
                scnt.subtract(digmap[8])

        if scnt['Z'] > 0:
            for i in range(scnt['Z']):
                ret.append(0)
                scnt.subtract(digmap[0])
                # reduce 4
        if scnt['W'] > 0:
            for i in range(scnt['W']):
                ret.append(2)
                scnt.subtract(digmap[2])

        if scnt['X'] > 0:
            for i in range(scnt['X']):
                ret.append(6)
                scnt.subtract(digmap[6])
                # reduce 4
        if scnt['F'] > 0:
            for i in range(scnt['F']):
                ret.append(5)
                scnt.subtract(digmap[5])
        if scnt['S'] > 0:
            for i in range(scnt['S']):
                ret.append(7)
                scnt.subtract(digmap[7])
        if scnt['R'] > 0:
            for i in range(scnt['R']):
                ret.append(3)
                scnt.subtract(digmap[3])
        if scnt['I'] > 0:
            for i in range(scnt['I']):
                ret.append(9)
                scnt.subtract(digmap[9])
        if scnt['N'] > 0:
            for i in range(scnt['N']):
                ret.append(1)
                scnt.subtract(digmap[1])
        # print(scnt)
    return "".join(list(map(str, sorted(ret))))

# tfile = "A-sample"
# tfile  = "A-small-attempt0 (1)"
tfile  = "A-large"
if __name__ == "__main__":
    with open(tfile+".in") as fin:
        sys.stdout = open(tfile+".out", "w")
        T = read(fin)
        for case in range(1, T+1):
            S = read(fin,str)
            ans = solve(case,S)
            print("Case #{}: {}".format(case, ans))




