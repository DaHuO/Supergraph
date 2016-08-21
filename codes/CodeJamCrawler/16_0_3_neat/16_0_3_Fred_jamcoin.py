import math
import random

from nzmath import *
from base import *


def ibase(n, radix=2, maxlen=None):
    r = []
    while n:
        n,p = divmod(n, radix)
        r.append('%d' % p)
        if maxlen and len(r) > maxlen:
            break
    r.reverse()
    return ''.join(r)

def gen_base2(length):
    for i in xrange(2**(length-2)):
        yield ibase(2**(length-1) + 1 + i*2)

def any_prime(nbs):
    for nb in nbs:
        if prime.primeq(nb):
            return True
    return False

def any_prime_approx(nbs):
    for nb in nbs:
        if prime.millerRabin(nb):
            return True
    return False

def factor(n, fmax=None):
    if not fmax:
        fmax = int(math.sqrt(n)) +1

    for d in xrange(2, fmax):
        if n % d == 0:
            return d

class CoinJamSolver (CodeJamSolver):
    def read_instance(self, f):
        return map(int, f.readline().split())

    def solve_instance(self, input):
        N, J = input

        count = 0
        out_lines = []
        for c in gen_base2(N):
            bases = [int(c, base=b) for b in range(2,11)]

            if any_prime_approx(bases):
                continue

            if any_prime(bases):
                continue

            factor_candidates = [factor(b, fmax=1000000) for b in bases]
            if not any(map(lambda f:f==None, factor_candidates)):
                # print c, factor_candidates
                out_lines.append('%s %s' % (c, ' '.join('%d' % f for f in factor_candidates)))

                count +=1
                if count == J:
                    break
        return '\n' + ('\n'.join(out_lines))

if __name__ == '__main__':
    solver = CoinJamSolver()
    solver.run()

    # print solver.solve_instance((32,50))
    # for i in range(100000000,100100000):
    #     is_probable_prime(i)
