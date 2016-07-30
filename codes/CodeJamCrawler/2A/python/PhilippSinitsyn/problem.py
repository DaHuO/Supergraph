import sys
import os
import math

# in = sys.stdin
fin = open('A-large.in')
# fout = sys.stdout
fout = open('out_1', 'w')

def expand(st, n, p, r, s):
    if len(st) == 2 ** n:
        return st
    st2 = ''
    rf, pf, sf = 0, 0, 0
    for sym in st:
        if sym == 'p':
            st2 += 'pr'
            pf += 1
            rf += 1
        elif sym == 'r':
            st2 += 'rs'
            rf += 1
            sf += 1
        elif sym == 's':
            st2 += 'ps'
            pf += 1
            sf += 1
    if (pf > p) or (rf > r) or (sf > s):
        raise TypeError('Pew')
    return expand(st2, n, p, r, s)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

def perplex(n, x):
    x2 = ''
    for i in range(2, n+1):
        for ch in chunks(x, 2 ** i):
            a = ch[:int(len(ch) / 2)]
            b = ch[int(len(ch) / 2):]
            if a < b:
                x2 += (a + b)
            else:
                x2 += (b + a) 
        x = x2
        x2 = ''
    return x

def solve(n, p, r, s):
    ans = []
    for sym in ['r', 'p', 's']:
        try:
            ans.append(expand(sym, n, p, r, s))
        except TypeError:
            continue
    if ans:
        return min(map(lambda x: perplex(n, x), ans)).upper()
    else:
        return 'Impossible'

if __name__ == '__main__':
    count = int(fin.readline().strip())

    for i in range(count):
        n, r, p, s = map(int, fin.readline().strip().split())
        result = solve(n, p, r, s)
        fout.write('Case #%s: %s\n' % (i + 1, result))


