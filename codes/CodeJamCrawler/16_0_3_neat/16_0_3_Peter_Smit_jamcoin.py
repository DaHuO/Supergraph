import sys

N=16
J=50

N=32
J=500

UPPER=17
a = [None] * 2**UPPER

a[0] = 0
a[1] = 1
a[2] = None

primes = []


for i in range(2,2**UPPER):
    if a[i] is None:
        primes.append(i)
        a[i] = i
        for j in range(i, 2**UPPER, i):
            a[j] = i

print("Case #1:")


num_test_primes = 10000
count = 0
for n in range(2**(N-1)+1, 2**N, 2):
    if count >= J:
        break

    b = "{0:b}".format(n)

    j = [int(b, base=base) for base in range(2, 11)]

    evidence = []
    for i in j:
        ok = False
        for p in primes[:num_test_primes]:
            if i > p and i % p == 0:
                evidence.append(p)
                ok = True
                break
        if not ok:
            break

    if len(evidence) == 9:
        print("{} {}".format(b, " ".join(str(e) for e in evidence)))
        count += 1

print("{} printed".format(count), file=sys.stderr)