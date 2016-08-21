__author__ = 'jcode'
import math
def check_prime(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

T = raw_input()
n, count = raw_input().split(" ")
n = int(n)
count = int(count)

vals = []
jamcoins = []
import datetime
start = datetime.datetime.now()
for i in xrange(2**(n-1), 2**n):
    val = (str(bin(i))[2:])
    if len(val) == n and val[0] == "1" and val[-1] == "1":
        base_vals = []
        for q in range(2, 11):
            num = int(val, q)
            base_vals.append(num)
            isPrime = False
            if check_prime(num):
                isPrime = True
                break
        if not isPrime:
            divisors = []
            for b in base_vals:
                for a in xrange(2, int(math.sqrt(b))):
                    if b % a == 0:
                        divisors.append(a)
                        break
            jamcoins.append((val, divisors))

    if len(jamcoins) >= count:
        break

print "Case #1:"
for jamcoin in jamcoins:
    print jamcoin[0], ' '.join(str(j) for j in jamcoin[1])

