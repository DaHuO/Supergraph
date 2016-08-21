from heapq import *
from string import ascii_uppercase
from collections import defaultdict

def valid(Q):
    if not Q:
        return True
    summ = sum(-i for i, _ in Q)
    maxx = max(-i for i, _ in Q)
    return maxx / summ <= 0.5

for case in range(int(input())):
    N = int(input())
    Q = []
    sen = map(int, input().split())
    for i, s in enumerate(sen):
        heappush(Q, (-s, ascii_uppercase[i]))
    room = defaultdict(int)
    tmp = []
    ans = []
    while Q:
        n, p = heappop(Q)
        n *= -1
        room[p] += 1
        if n > 1:
            heappush(Q, (-n+1, p))
        if valid(Q):
            tmp.append(p)
            ans.append(''.join(tmp))
            tmp = []
        else:
            tmp.append(p)
    print("Case #%d: " % (case+1), ' '.join(ans))
