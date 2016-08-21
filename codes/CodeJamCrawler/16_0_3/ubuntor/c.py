import sys
import itertools
from sage.all import is_prime, factor
N = 32
J = 500
out = 'Case #1:\n'
found = 0
for i in itertools.product('01',repeat=N-2):
    n = '1'+''.join(i)+'1'
    l = []
    for j in range(2,11):
        if is_prime(int(n,j)):
            break
        l.append(str(factor(int(n,j))[0][0]))
    else:
        print("found",n,l)
        out += '{} {}\n'.format(n,' '.join(l))
        found += 1
        if found >= J:
            break
open('C.out','w').write(out)
