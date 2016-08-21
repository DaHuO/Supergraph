__author__ = 'drathier'

r = lambda: [line.split() for line in input()]


def m():
    n = input()
    a = []
    for _ in range(n):
        a += [input()]

    num = 1
    for i in a:
        print "Case #{0}: {1}".format(num, s(i))
        num+=1


def nums(a):
    res = 0
    while a >= 10:
        num = a % 10
        res |= 1 << num
        a -= num
        a /= 10
        #print "nums", a, num, "<{0:010b}>".format(res)
    res |= 1 << (a % 10)
    #print "nums", a, "<{0:010b}>".format(res)
    return res


def s(a):
    got = 0
    last = -1
    for i in xrange(1, 2 ** 30):
        n = nums(i*a)
        if n != got:
            last = i
        got |= n

        #print "got", got, "<{0:010b}>".format(got), i, a, "<{0:010b}>".format(n)
        if got >= 2 ** 10 - 1:
            return i*a
        if i - last > 10 ** 6:
            return "INSOMNIA"
    return "INSOMNIA"


m()
"""
#for i in range(100):
#    print "#### Nums ", i, nums(i)
#1/0

from random import randint

# print 0, s(0), "INSOMNIA"
print 1, s(1), 10
print 2, s(2), 90
print 11, s(11), 110
print 1692, s(1692), 5076
for i in range(6):
    print 10 ** i, s(10 ** i), "?"
for i in range(200):
    print "seq", i, s(i)

for i in range(10000):
    r = randint(0, 10 ** 6)
    print "rand", i, r, s(r)
#1 / 0
"""