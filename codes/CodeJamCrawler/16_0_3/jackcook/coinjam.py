from itertools import count, islice, product
from math import sqrt
import sys

fp = file(sys.argv[1])
t = int(fp.next())

of = file("out.txt", 'w+')

c = {}
def is_prime(n):
    if n in c:
        return c[n]
    else:
        c[n] = n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
        return c[n]

d = {}
def find_divisor(n):
    if n in d:
        return d[n]
    else:
        d[n] = n / min(set(reduce(list.__add__,
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0))))
        return d[n]

for i in range(t):
    (n, j) = [int(x) for x in fp.next().split()]
    coins = ["1%s1" % x for x in map("".join, product("10", repeat=(n-2)))]
    valid = []
    nums = []
    for coin in coins:
        q = []

        v = True
        for p in range(9):
            o = int(coin, p + 2)
            if is_prime(o):
                v = False
                break
            else:
                q.append(find_divisor(o))

        if v:
            print "jamcoin found"
            valid.append(coin)
            nums.append(q)

        if len(valid) == j:
            break

    of.write("Case #%d:\n" % (i + 1))
    for w in range(len(valid)):
        of.write("%s %s\n" % (valid[w], " ".join([str(x) for x in nums[w]])))

of.close()
