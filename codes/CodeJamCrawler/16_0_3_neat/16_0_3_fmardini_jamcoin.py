import os, sys, random

N, J = 32, 500
bases = range(2, 11)
powers = {}
for b in bases:
    a = [1]
    for i in range(1, N):
        a.append(a[-1] * b)
    powers[b] = a

def random_set():
    res = []
    for i in range(1, N - 1):
        if random.random() < 0.5:
            res.append(i)
    return res

def gen_numbers():
    s = random_set()
    ns = []
    for b, ps in powers.iteritems():
        n = ps[0] + ps[-1]
        n += sum(ps[i] for i in s)
        ns.append(n)
    return ns, s

primes = []
P = int(sum(powers[10]) ** 0.5) + 1
P = int(3.5e7)
sieve = [True] * (P + 1)
sieve[0] = sieve[1] = False
for i in range(2, P + 1):
    if sieve[i]:
        primes.append(i)
        j = i + i
        while j < P + 1:
            sieve[j] = False
            j += i

def prime_test(n):
    u = int(n ** 0.5)
    for i in xrange(len(primes)):
        if primes[i] > u: break
        if n % primes[i] == 0: return primes[i]
    return 1

print("Case #1:")

uniq = set()
res = []
iters = 0
while len(res) < J:
    iters += 1
    # if iters % 1000 == 0: print(iters)
    ns, s = gen_numbers()
    factors = []
    for n in ns:
        f = prime_test(n)
        if f == 1: break
        factors.append(f)
    if len(factors) == 9 and ns[0] not in uniq:
        uniq.add(ns[0])
        res.append((ns[-1], factors))
        print("{} {}".format(ns[-1], ' '.join(map(str, factors))))
