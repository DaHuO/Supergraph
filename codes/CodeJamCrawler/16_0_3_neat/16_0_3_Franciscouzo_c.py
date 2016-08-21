import random

def get_primes(max_):
    primes = [2]
    for i in xrange(3, max_ + 1):
        if not any(i % p == 0 for p in primes):
            primes.append(i)
    return primes


primes = get_primes(1000)
primes_s = set(primes)

def gen_coinjam(l):
    return '1{}1'.format(''.join(str(random.randint(0, 1)) for i in xrange(l - 2)))

found = []

print 'Case #1:'
while len(found) < 500:
    coinjam = gen_coinjam(32)
    if coinjam in found:
        continue
    possible = []
    for base in xrange(2, 11):
        n = int(coinjam, base)
        if n not in primes_s:
            for p in primes:
                if n % p == 0 and n != p:
                    possible.append(p)
                    break
            else:
                break
    else:
        found.append(coinjam)
        print coinjam, ' '.join(map(str, possible))
