import fileinput
import itertools

for e, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        continue
    N, J = (int(c) for c in line.strip().split())

    limit = int(int("1"*N)**0.5) + 1
    sieve = [True] * limit
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i + i, limit, i):
                sieve[j] = False
    primes = [i for i in range(2, limit) if sieve[i]]

    candidates = [((1, ) + inner_coin + (1, ), list()) for inner_coin
                  in itertools.product(range(2), repeat=(N - 2))]

    for base in range(2, 11):
        new_candidates = []
        for candidate in candidates:
            v = 0
            coin, divisors = candidate
            for c in coin:
                v *= base
                v += c
            for i in itertools.takewhile(lambda p: p <= int(v**.5) + 1, primes):
                if v % i == 0:
                    divisors.append(i)
                    new_candidates.append((coin, divisors))
                    break

        candidates = new_candidates

    print "Case #{}:".format(e)
    for candidate in candidates[:J]:
        coin, divisors = candidate
        print "".join(str(x) for x in coin), " ".join(str(x) for x in divisors)
