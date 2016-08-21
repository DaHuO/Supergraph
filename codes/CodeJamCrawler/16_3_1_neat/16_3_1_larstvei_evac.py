from sys import stdin
from collections import Counter

for i in range(int(stdin.readline())):
    a = Counter()
    p = int(stdin.readline())
    ps = map(int, stdin.readline().split())

    for c, pi in zip([chr(x+ord('A')) for x in range(p)], ps):
        a[c] = pi

    res = []

    while len(a):
        c = a.most_common()[0][0]
        a[c] -= 1
        if a[c] == 0:
            del a[c]
        res.append(c)
        if sum(a.values()) == 2:
            continue

        c = a.most_common()[0][0]
        a[c] -= 1
        if a[c] == 0:
            del a[c]
        res[-1] = res[-1] + c

    print ('Case #%d: ' + ' '.join(res)) % (i+1)
