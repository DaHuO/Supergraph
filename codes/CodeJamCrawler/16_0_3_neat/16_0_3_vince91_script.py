import math

T = int(raw_input())
N, J = [int(x) for x in raw_input().split()]


def prime_least(n):
    if n % 2 == 0:
        return 2
    m = math.sqrt(n)
    for i in xrange(3, int(min(m, 100000)), 2):
        if n % i == 0:
            return i
    return -1

a = 2**(N-1) + 1
jamcoins = []

while len(jamcoins) < J:
    a_2 = "{0:b}".format(a)
    divisors = []
    for k in xrange(2, 11):
        p = prime_least(int(a_2, k))
        if p != -1:
            divisors.append(p)
        else:
            break
    if len(divisors) == 9:
        jamcoins.append((a_2, divisors))
    a += 2


def check(jamcoin):
    s, divisor = jamcoin

    for k in xrange(2, 11):
        if int(s, k) % divisor[k-2] != 0:
            print("wroooonnng")


print "Case #1:"
for j in jamcoins:
    print "%s %s" % (j[0], " ".join([str(d) for d in j[1]]))
