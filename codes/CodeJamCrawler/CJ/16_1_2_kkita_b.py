#!/usr/bin/python
import itertools

def isSort(l):
    if all(l[i] <= l[i+1] for i in range(len(l)-1)):
        return True
    return False

def verify_map(m, l):
    m = [sorted(list(e)) for e in m]
    mT = [sorted(list(e)) for e in list(zip(*m))]
    total = m + mT
    d = list(l)
    for e in l:
        if e in total:
            total.remove(e)
    if (len(total) == 1):
        return total
    return False
"""

def find_missing(m, l):
    print("find_missing")
    mT = map(list,zip(*m))
    total = list(m) + list(mT)
    print(mT)
    print(l)
    print(total)
    res = l
    for i in total:
        if i in res:
            res.remove(i)
    return res
    """


T = int(input())
result = []
for case in range(0,T):
    N = int(input())
    lists = []
    for i in range(2*N-1):
        temp = list(map(int, input().split()))
        lists.append(temp)
    for m in itertools.combinations(lists, N):
        x = verify_map(m,lists)
        if (x):
            result.append(((case+1), x[0]))
            break

for (x,y) in result:
    print("Case #%d: " % (x), end="")
    print(" ".join(str(e) for e in y))
