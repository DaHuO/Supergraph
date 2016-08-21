from math import sqrt

def prime(n):
    for i in range(3, int(sqrt(n)+1), 2):
        if n % i == 0:
            return i
    return 0

def no_prime(s):
    factors = []
    for i in range(2, 11):
        temp = prime(int(s, i))
        if temp == 0:
            return factors
        factors.append(temp)
    return factors

count = 1
print "Case #1:"
for i in range(0b1000000000000001, 0b1111111111111111+1, 2):
#for i in range(0b100001, 0b111111+1, 2):
    s = bin(i)[2:]
    factors = no_prime(s)
    if len(factors) == 9:
        print s,
        print " ".join(map(str, factors))
        if count == 50:
            break
        count += 1
