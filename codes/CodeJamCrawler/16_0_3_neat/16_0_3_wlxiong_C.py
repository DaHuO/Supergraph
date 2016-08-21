import sys
import math
import array
import random
import itertools
import multiprocessing


def calc_primes(n):
    bitmap = array.array('i', (1,) * n)
    bitmap[0] = 0
    bitmap[1] = 0
    for i in range(n):
        if bitmap[i]:
            for j in range(i * 2, n, i):
                bitmap[j] = 0
    return [i for i in range(n) if bitmap[i]]

MAX = 12
primes = calc_primes(int(math.sqrt(10**MAX * 2)))
# print primes

def factor(x):
    for p in primes:
        if x % p == 0:
            return p
    return None


def fermat_test(x, n=100):
    def expmod(b, i, m):
        if i == 0:
            return 1
        if i % 2 == 0:
            return expmod(b, i / 2, m)**2 % m
        return expmod(b, i - 1, m) * b % m
    for _ in range(n):
        r = random.randint(1, x-1)
        if expmod(r, x, x) != r:
            return False
    return True


def random_product(*args, **kwds):
    "Random selection from itertools.product(*args, **kwds)"
    pools = map(tuple, args) * kwds.get('repeat', 1)
    while True:
        yield tuple(random.choice(pool) for pool in pools)


base = [[pow(b, n) for n in range(33)] for b in range(2, 11)]
def eval_number(s, b):
    s = tuple(reversed(s))
    # print s, b
    return sum(x * y for x, y in zip(s, base[b-2][:len(s)]))

def mine_jamcoin(input):
    N, J = input
    C = []
    if N <= MAX:
        C = itertools.product((0, 1), repeat=N)
    else:
        C = random_product((0, 1), repeat=N)
    res = []
    for x in C:
        # print "x", x
        if x[0] == x[-1] == 1:
            ff = []
            for b in range(2, 11):
                num = eval_number(x, b)
                if N > MAX and fermat_test(num):
                    break
                f = factor(num)
                if f is None:
                    ff = []
                    break
                ff.append(f)
            else:
                res.append([''.join(map(str, x))] + map(str, ff))
                if len(res) >= J:
                    return '\n'.join(' '.join(r) for r in res)
    raise Exception("no answer")


def main():
    T = int(sys.stdin.readline())
    inputs = [map(int, sys.stdin.readline().split()) for _ in range(T)]
    cores = multiprocessing.cpu_count() / 2
    p = multiprocessing.Pool(max(1, cores - 1))
    try:
        outputs = p.map(mine_jamcoin, inputs)
    except KeyboardInterrupt:
        p.terminate()
    # outputs = map(jamcoin, inputs)
    for t, r in enumerate(outputs):
        print >> sys.stderr, "Case #%d:" % (t + 1)
        print "Case #%d:" % (t + 1)
        print r


if __name__ == '__main__':
    main()
