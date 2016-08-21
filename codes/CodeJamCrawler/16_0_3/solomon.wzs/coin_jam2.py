#!/usr/bin/python2


import math


prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 113,
              193, 241, 257, 337, 353, 401, 433, 449, 577, 593, 641,
              673, 769, 881, 929, 977, 1009, 1153, 1201, 1217, 1249,
              1297, 1361, 1409, 1489, 1553, 1601, 1697, 1777, 1873,
              1889, 2017, 2081, 2113, 2129, 2161, 2273, 2417, 2593,
              2609, 2657, 2689, 2753, 2801, 2833, 2897, 3041, 3089,
              3121, 3137, 3169, 3217, 3313, 3329, 3361, 3457, 3617,
              3697, 3761, 3793, 3889, 4001, 4049, 4129, 4177, 4241,
              4273, 4289, 4337, 4481, 4513, 4561, 4657, 4673, 4721,
              4801, 4817, 4993, 5009, 5153, 5233, 5281, 5297, 5393,
              5441, 5521, 5569, 5857, 5953, 6113, 6257, 6337, 6353,
              6449, 6481, 6529, 6577, 6673, 6689, 6737, 6833, 6961,
              6977, 7057, 7121, 7297, 7393, 7457, 7489, 7537, 7649,
              7681, 7793, 7841, 7873, 7937, 8017, 8081, 8161, 8209,
              8273, 8353, 8369, 8513, 8609, 8641, 8689, 8737, 8753,
              8849, 8929, 9041, 9137, 9281, 9377, 9473, 9521, 9601,
              9649, 9697, 9857]


def montgomery(n, p, m):
    r = n % m
    k = 1
    while p > 1:
        if p & 1 != 0:
            k = (k * r) % m
        r = (r * r) % m
        p /= 2
    return (r * k) % m


def is_prime(n):
    if n < 2:
        return False

    for i in xrange(len(prime_list)):
        if n % prime_list[i] == 0 or montgomery(prime_list[i], n - 1, n) != 1:
            return False

    return True


def f(n, j):
    res = ""
    for x in xrange(int("1%s1" % ("0" * (n - 2)), 2),
                    int("1%s1" % ("1" * (n - 2)), 2) + 1,
                    2):
        s = bin(x)[2:]
        ok = True
        for i in xrange(2, 11, 1):
            n = int(s, i)
            if is_prime(n):
                ok = False
                break

        if ok:
            l = [0] * 9
            for i in xrange(2, 11, 1):
                n = int(s, i)
                ok = False
                for k in xrange(2, min(int(math.sqrt(n)), 1000000)):
                    if n % k == 0:
                        ok = True
                        l[i - 2] = str(k)
                        break
                if not ok:
                    break
            if ok:
                res += "%s %s\n" % (s, " ".join(l))
                j -= 1

        if j == 0:
            return res[0:len(res)-1]


import sys
fd = open(sys.argv[1], "rb")
t = int(fd.readline().strip())
for i in xrange(1, t + 1):
    line = fd.readline().strip()
    arr = line.split(" ")
    n = int(arr[0])
    j = int(arr[1])
    res = f(n, j)
    print "Case #%d:\n%s" % (i, res)
fd.close()
