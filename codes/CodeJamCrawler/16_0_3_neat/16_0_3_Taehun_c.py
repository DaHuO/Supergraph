from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def dec_to_base(dec, base):
    return int(dec, base)

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print "Case #1:"

n = 16 
j = 50

ss = "0b" + ''.join(['1' for x in xrange(n-2)])
ts = []
for i in xrange(int(ss, 2) + 1):
    ts.append("{0:014b}".format(i))

for ss in ts:
    s = '1' + ss + '1'
    jam = []
    is_prime = False
    for base in xrange(2, 11):
         jam.append(dec_to_base(s, base))
    for jj in jam:
        if isPrime(jj):
            is_prime = True

    if is_prime:
        continue

    print s,

    for i in xrange(len(jam)):
        for d in xrange(3, jam[i]):
            if jam[i] % d == 0:
                print d,
                break
    print
    j = j - 1

    if j == 0:
        break
