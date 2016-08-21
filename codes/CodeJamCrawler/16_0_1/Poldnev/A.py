from functools import *

inf = open('A-large.in')
ouf = open('output.txt', 'w')
input = lambda: inf.readline().strip()
print = partial(print, file = ouf)


def f(x):
    res = 0
    digs = set()
    cur = 0
    while len(digs) < 10:
        res += 1
        cur += x
        digs.update(str(cur))
    return res


def solve():
    n = int(input())
    if n == 0:
        print('INSOMNIA')
    else:
        print(f(n) * n)
    
    
tests = int(input())
for z in range(tests):
    print("Case #{}: ".format(z + 1), end = '')
    solve()

ouf.close()