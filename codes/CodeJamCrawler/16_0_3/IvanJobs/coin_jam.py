import itertools
import math

in_file, out_file = 'C-small-attempt0.in', 'C-small-attempt0.out'


N = 2**17 + 10

# 1 stands for prime
h = [1,] * N

h[0], h[1] = 0, 0

i = 2

while i < N:
    # i is 1, we delete items based on i
    for j in xrange(2*i, N, i):
        h[j] = 0

    # after i is done, continue with next item
    i += 1
    while i < N and h[i] == 0:
        i += 1

res = []
for i in xrange(N):
    if h[i] == 1:
        res.append(i)

primes = set(res)

def is_prime(v):
    if v > 2 and v % 2 == 0:
        return False
    elif v <= 1:
        return False
    else:
        for i in xrange(2, int(math.sqrt(v))):
            if v % i == 0:
                return False
        return True

with open(out_file, 'w') as fout:
    ret = []
    for v in xrange(0, 2**14):

        v2 = 2**15 + 1 + v*2

        # make big number
        num = []
        v22 = v2
        while v22 > 0:
            num.append(v22%2)
            v22 /= 2

        good = True
        cache = []
        for b in range(2, 11):

            curr = 0

            for i in range(16):
                curr += b**i * num[i]

            cache.append(curr)
            if is_prime(curr):
                good = False
                break
        if good:
            # here, we need to collect one item
            one = []
            one.append(''.join(list(bin(v2))[2:]))

            for dv in cache:
                for i in xrange(2, int(math.sqrt(dv))):
                    if dv % i == 0:
                        one.append(str(i))
                        break


            ret.append(one)

            if len(ret) >= 50:
                break
    fout.write('Case #1:\n')
    for batch in ret:
        fout.write(' '.join(batch) + '\n')

