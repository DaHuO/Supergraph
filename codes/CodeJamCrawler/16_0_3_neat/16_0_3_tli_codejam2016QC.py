import math
def prime_factor(n):
    for i in xrange(2, 10):
        if n % i == 0:
            return i
    return None

print "Case #1:"

count = 0

for i in xrange(2**31 + 1, 2 ** 32, 2):
    representation = [0 for j in xrange(32)]

    j = i
    for k in xrange(32):
        representation[k] = j % 2
        j /= 2

    factors = []
    for b in xrange(2, 11):
        s = 0
        m = 1
        for k in xrange(32):
            s += m * representation[k]
            m *= b

        factor = prime_factor(s)
        if factor != None:
            factors.append(factor)
        else:
            break

    if len(factors) == 9:
        print s,
        for f in factors:
            print f,
        count += 1

        print

    if count == 500:
        break

