t = 1
n = 16
j = 50

def sieve(limit):
    a = [0,0] + [-1] * limit
    for (i, isprime) in enumerate(a):
        if isprime == -1:
            a[i] = -1
            for n in xrange(i*i, limit, i):
                a[n] = i
    return a

def divisorOf(n):
    if n == 2 or n == 3: return False
    for x in xrange(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return x
    return -1

def jamcoinDivisors(jamcoin):
    divisors = []
    for x in xrange(2,11):
        baseTenJamcoin = int(jamcoin, x)
        legalDivisor = divisorOf(baseTenJamcoin)
        if legalDivisor == -1:
            return False, None
        else:
            divisors.append(legalDivisor)
    return True, divisors

# Iterate through the legal combinations, terminate once n jamcoins have been
# found.
answers = []
for x in xrange(4, 2**n):
    jamcoin = bin(x)[2:].zfill(n)
    if jamcoin[0] == '1' and jamcoin[-1] == '1':
        result = jamcoinDivisors(jamcoin)
        if result[0] == True:
            answers.append([jamcoin] + [str(divisor) for divisor in result[1]])
        if len(answers) == j:
            break

print "Case #1:"
for x in answers:
    print ' '.join(x)


