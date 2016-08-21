sieve = (33333334) * [True]
primes = []

for i in range(2, 5774):
    if sieve[i]:
        primes.append(i)
        for j in range(2 * i, 33333334, i):
            if sieve[j]:
                sieve[j] = False
for i in range(5774, 33333334):
    if sieve[i]:
        primes.append(i)

def is_prime(n):
    for p in primes:
        if p >= n:
            return None
        if n % p == 0:
            return p

print("Case #1:")
cnt = 0
for i in range(2**15+1, 2**16, 2):
    s = "{:b}".format(i)
    divs = []
    for base in range(2, 11):
        d = is_prime(int(s, base))
        if d is None:
            break
        divs.append(d)
    else:
        print("%s %s" % (s, " ".join("%s" % k for k in divs)))
        cnt += 1
        if cnt == 50:
            break

