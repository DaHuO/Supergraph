#!/usr/bin/python
import sys
from string import maketrans
intab = "GL"
outtab = "10"
trantab = maketrans(intab, outtab)

# 1 1 1 : 1 1 1 1 1 1 1 1 1
# 1 1 0 : 1 1 1 1 1 1 1 1 0
# 1 0 1 : 1 1 1 1 0 1 1 1 1
# 1 0 0 : 1 1 1 1 0 0 1 0 0
# 0 1 1 : 0 1 1 1 1 1 1 1 1
# 0 1 0 : 0 1 0 1 1 1 0 1 0
# 0 0 1 : 0 0 1 0 0 1 1 1 1
# 0 0 0 : 0 0 0 0 0 0 0 0 0

def trans(column, K):
    return reduce(lambda x, y: x*K + y, column)+1

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, n):
        yield l[i:len(l):n]

def solve(s):
    K, C, S = map(int, s.split())
    filter_number = C * S
    if filter_number < K:
        return "IMPOSSIBLE" # filters cannot cover all tiles
    padding = C-(K%C)
    if padding == C:
        padding = 0
    tiles = [0] * padding + range(0, K)
    choose = list(chunks(tiles, len(tiles)/C))
    #print K, C, S, tiles
    #print choose
    choose = map(lambda x: str(trans(x, K)), choose)
    return " ".join(choose)

for i in range(1, int(raw_input())+1):
    print "Case #{}:".format(i), solve(raw_input())
sys.exit()
