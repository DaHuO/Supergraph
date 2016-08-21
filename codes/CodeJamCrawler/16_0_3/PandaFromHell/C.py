__author__ = 'vitaly'

import itertools
import random
import math

def gcd(a, b):
    while a != 0:
        a, b = b%a, a
    return b

def prime(x):
    ans = 1
    q = x - 1
    while (q % 2 == 0):
        q /= 2
    for i in range(1000):
        a = random.randrange(2, x - 1)
        if gcd(a, x) != 1:
            return gcd(a, x)
        if pow(a, x - 1, x) != 1:
            return 0
        a = pow(a, q, x)

        if (a != 1):
            while a != 1 and a != x - 1:
                a = (a * a) % x
            if a == 1:
                return 0
    return ans

def f(n, k):
    for i in xrange(0, 2**(n - 2)):
        if k == 0:
            return 1
        s = bin(i)[2:]
        while len(s) != n - 2:
            s = "0" + s
        s = "1" + s + "1"
        cnt = 0
        for b in range(2, 11):
            num = int(s, base = b)
            p = prime(num)
            if p == 1:
                cnt = 1
                break
        if (cnt == 0):
            res = s
            k -= 1
            for b in range(2, 11):
                num = int(s, base = b)
                p = prime(num)
                if p == 0:
                    j = 2
                    while True:
                        if num % j == 0:
                            p = j
                            break
                        j += 1
                res += " " + str(p)
            print res
            file.write(res+'\n')

def f1(n ,k):
    for i in xrange(0, 2**(n - 2)):
        if k == 0:
            return 1
        s = bin(i)[2:]
        while len(s) != n - 2:
            s = "0" + s
        s = "1" + s + "1"
        cnt = 0
        for b in range(2, 11):
            num = int(s, base = b)
            ok = False
            for d in range(2, 20):
                if num % d == 0:
                    ok = True
                    break
            if ok == False:
                cnt = 1
                break
        if (cnt == 0):
            res = s
            k -= 1
            for b in range(2, 11):
                num = int(s, base = b)
                p = 1
                for d in range(2, 20):
                    if num % d == 0:
                        p = d
                        break
                res += " " + str(p)
            print(res)
            #file.write(res+'\n')



t = int(raw_input())
#file = open("res.txt", "w")
#t = 0
for i in range(1):
    q = raw_input()
    _ = q.find(" ")
    n = int(q[:_])
    k = int(q[_+1 :])
    #n = 32
    #k = 500

    print "Case #{}:".format(i + 1)
    #file.write("Case #{}:\n".format(i + 1))
    f1(n, k)