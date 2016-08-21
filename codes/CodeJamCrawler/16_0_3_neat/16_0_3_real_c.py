import sys, itertools, collections, random, math
sys.setrecursionlimit(10000)


M = 10 ** 6 # 7
is_prime = [True] * (M + 1)

primes = []


for i in xrange(2, M + 1):
    if not is_prime[i]:
        continue

    for j in range(i + i, M + 1, i):
        is_prime[j] = False

    primes.append(i)


#N = 16
#J = 50
N = 32
J = 500


def is_composite(num):
    for p in primes:
        if num % p == 0 and p < num:
            return p

    return None


print 'Case #1:'

ans = []
used = set()

while len(ans) < J:
    s = [1] + [random.choice([0, 1]) for _ in xrange(N - 2)] + [1]

    if tuple(s) in used:
        continue

    proof = []
    for base in range(2, 11):
        num = sum([base ** i * s[i] for i in xrange(len(s))])
        f = is_composite(num)
        if f is None:
            break

        proof.append(f)

    if len(proof) == 9:
        ret = ''.join(map(str, reversed(s))) + ' '
        ret += ' '.join(map(str, proof))

        ans.append(ret)
        print ret

        used.add(tuple(s))
