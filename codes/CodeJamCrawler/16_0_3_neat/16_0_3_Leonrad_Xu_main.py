import sympy
import random

N = 32
J = 500

def check(x):
    for base in xrange(2, 11):
        v = 0
        b = 1
        t = x
        while t > 0:
            if t % 2 == 1:
                v += b
            b *= base
            t /= 2
        if sympy.isprime(v):
            return False
    return True


def info(x):
    res = []
    for base in xrange(2, 11):
        v = 0
        b = 1
        t = x
        while t > 0:
            if t % 2 == 1:
                v += b
            b *= base
            t /= 2
        res.append(str(sympy.pollard_rho(v)))
    return ' '.join(res)


print 'Case #1:'
u = (1 << (N - 1)) + 1
for i in xrange(J):
    step = 2
    while not check(u):
        u += step
        if step == 1024:
            step += 2
        else:
            step *= 2

    print '{0:b}'.format(u), info(u)
    u += 2
