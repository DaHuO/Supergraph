from functools import partial

def fractileIndexing(x, ith, K):
    return (x-1)*K + ith

def solve(K, C, S):
    indices = list(range(1, K+1))

    for i in range(C-1):
        indices = [fractileIndexing(x, i+1, K) for i,x in enumerate(indices)]

    return indices

for i,_ in enumerate(range(int(input()))):
    K,C,S = map(int, input().split())
    print('Case #{}: {}'.format(i+1, " ".join(str(x) for x in solve(K,C,S)) ))
#
# LGL
# 123
#
# LGLGGGLGL
# 123456789
# 1   2   3
#
# LGLGGGLGLGGGGGGGGGLGLGGGLGL
# 123456789012345678901234567
# 1            2            3
#
# 1 -> 1 -> 1
# 2 -> 5 -> 14
# 3 -> 9 -> 27
#
# 2*3 + 3
# 8*3 + 3
#
# 0*3 + 1
#
# 1*3+2
# 4+3 + 2