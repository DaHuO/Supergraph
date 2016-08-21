from itertools import chain
from collections import Counter
tests= int(input())
for i in range(0, tests):
    n = int(input())
    both = []
    for q in range(0, 2*n-1):
        both.append(input().split())
##    firsts = []
##    for w in range(0, len(both)):
##        firsts.append(both[w][0])
##    lasts = []
##    for e in range(0, len(both)):
##        lasts.append(both[e][-1])
##    start = min(firsts)
##    stop = max(lasts)
##    starts = []
##    stops = []
##    for r in range(0, len(both)):
##        try:
##            s = both[r].index(start)
##            starts.append(r)
##        except ValueError:
##            pass
##        try:
##            s = both[r].index(stop)
##            stops.append(r)
##        except ValueError:
##            pass
    a = Counter(chain.from_iterable(both))
    d = dict(a)
    odds = []
    for key in d:
        if d[key] % 2 == 1:
            odds.append(key)
    for u in range(0, len(odds)):
        odds[u] = int(odds[u])
    odds.sort()
##    print(odds)
    final = ""
    for j in range(0, len(odds)):
        if j == len(odds) - 1:
            final += str(odds[j])
        else:
            final += str(odds[j]) + " "
    print("Case #" + str(i+1) + ": " + final)
##    for t in range(0, len(both)):
##        print(Counter(both[t]))
##    print(starts, stops)
