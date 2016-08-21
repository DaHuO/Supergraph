from functools import *

inf = open('B-large.in')
ouf = open('output.txt', 'w')
input = lambda: inf.readline().strip()
print = partial(print, file = ouf)


def solve():
    s = input().strip()
    g = 0
    for i, c in enumerate(s):
        g += (i > 0 and c != s[i - 1])
    if (g % 2 == 0 and s[0] == '-') or (g % 2 == 1 and s[0] == '+'):
        g += 1
    print(g)
    
    
tests = int(input())
for z in range(tests):
    print("Case #{}: ".format(z + 1), end = '')
    solve()

ouf.close()