from itertools import product
from math import sqrt

def p(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return str(i)

def jammy(n):
    d = []
    for base in range(2, 11):
        d.append(p(int(n, base)))
        if d[-1] is None:
            return
    return d

def jam(n, j):
    jams = []
    for x in product('01', repeat=n-2):
        num = '1{}1'.format(''.join(x))
        r = jammy(num)
        if r is not None:
            jams.append('{} {}'.format(num, ' '.join(r)))
            if len(jams) == j:
                break

    print('Case #1:')
    print('\n'.join(jams))

jam(16, 50)
