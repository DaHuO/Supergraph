__author__ = 'shiva'
import random
def jamcoin(n, f):
    l = [1]
    for i in range(n-2):
        l.append(random.choice([0, 1]))
    l.append(1)
    l = ''.join(map(str, l))
    if l in f:
        return False
    h = []
    for k in range(2, 11):
        u = int(l, k)
        for p in range(2, 1000):
            if float(u)%float(p) == 0 and u != p:
                h.append(str(p))
                break
            elif p > 98:
                return False
    return l, h

def testcases(n, j):
    f = []
    c = 0
    while c < j:
        l = jamcoin(n, f)
        if not l:
            continue
        f.append(l[0])
        f.append(' '.join(l[1]))
        c += 1
    return f

o = open("output.txt",'w')

n, j = 16, 50

print>>o, "Case #1:"
lines = testcases(n, j)

for q in range(0, len(lines), 2):
    print>>o, lines[q] + " " + lines[q+1]
    print lines[q] + " " + lines[q+1]