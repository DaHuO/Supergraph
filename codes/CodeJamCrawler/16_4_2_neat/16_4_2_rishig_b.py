import sys
from numpy import array
from itertools import combinations

def prod(ps):
    k = len(ps)
    poly = [1]
    for p in ps:
        add = [0] + [(1-p)*x for x in poly]
        poly = [p*poly[i] + add[i] for i in range(len(poly))] + [add[-1]]
    return poly[k/2]

def run(N,K,lst):
    return max(prod(x) for x in combinations(lst, K))

    # m = [0]
    # k = K
    # lst.sort()
    # m.append(prod(lst[:k/2] + lst[-k/2:]))
    # B = [x for x in lst if x > .5]
    # b = len(B)
    # S = [x for x in lst if x <= .5]
    # s = len(S)
    # if b < k:
    #     for i in range(k-b+1):
    #         m.append(prod(B + S[:i] + S[-i:]))
    # if s < k:
    #     for i in range(k-s+1):
    #         m.append(prod(S + B[:i] + B[-i:]))
    # return max(m)

fin = file(sys.argv[1])
T = int(fin.readline().strip())
for i in range(1,T+1):
    N,K = [int(x) for x in fin.readline().strip().split()]
    lst = [float(x) for x in fin.readline().strip().split()]
    ans = run(N,K, lst)
    print('Case #%d: %s' % (i, ans))
