import sys
import itertools as it
from math import floor, sqrt

divisor = lambda n: next(i for i in range(2, floor(sqrt(n))) if n % i == 0)

for x in range(1, int(sys.stdin.readline()) + 1):
    N, J = map(int, sys.stdin.readline().strip().split())
    print('Case #{}:'.format(x))
    jcs = 0
    for jc in it.product('01', repeat=N-2):
        jc = '1' + ''.join(jc) + '1'
        try:
            divs = [divisor(int(jc, i)) for i in range(2, 11)]
        except:
            continue
        if len(divs) == 9:
            print(jc, ' '.join(map(str, divs)))
            jcs += 1
        if jcs == J:
            break
