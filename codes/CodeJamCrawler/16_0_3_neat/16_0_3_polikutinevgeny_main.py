from itertools import product
from math import sqrt, ceil
inf = open('input.txt', 'r')
ouf = open('output.txt', 'w')
t = int(inf.readline())
n, j = map(int, inf.readline().split())
ouf.write('Case #1:\n')
p = ['1' + ''.join(i) + '1' for i in product('01', repeat=n-2)]
for i in p:
    print(i)
    if j == 0:
        break
    ds = []
    for b in range(2, 11):
        t = int(i, b)
        for d in range(2, ceil(sqrt(t))):
            if t % d == 0:
                ds.append(d)
                break
    if len(ds) == 9:
        j -= 1
        ouf.write('{} {} {} {} {} {} {} {} {} {}\n'.format(i, *ds))
inf.close()
ouf.close()