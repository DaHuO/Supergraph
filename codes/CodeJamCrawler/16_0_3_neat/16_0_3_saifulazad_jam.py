__author__ = 'Azad'
import math
l = []

def isprime(n):

    if n ==2:
        return 0

    if n%2==0:
        return 2

    else:

        for x in xrange(3, int(math.sqrt(n))+1,2):

            if n%x == 0 : return x


    return 0


def conv(n, b):

    r = n[::-1]

    s =0
    for x in range(len(r)):

        s = s+ int(r[x]) * b**x
        #print int(r[x]) * b**x

    return s

n = 14
for x in xrange(2**n):
    p = bin(x)[2:]
    t = n-len(p)

    r = t*'0' + p
    #print r
    l.append('1'+r+'1')

c =0

for r in l:

    y = [conv(r,x) for x in xrange(2,11)]

    t = [isprime(x) for x in y]

    if all(t):
        c +=1
        q = r+ ' '+' '.join([str(x) for x in t])
        print q

    if c == 50:break