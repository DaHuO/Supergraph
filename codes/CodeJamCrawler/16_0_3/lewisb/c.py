import sys
import math
lines = sys.stdin.read().splitlines()
t = int(lines[0])
cases = []
for i in range(t):
    cases.append(lines[i + 1])

def get_factor(n):
    for i in range(2, int(math.ceil(math.sqrt(n)) + 1)):
        if n % i == 0: return i

for counter, case in enumerate(cases):
    sys.stdout.write('Case #%d:\n' % (counter + 1))
    info = case.split(" ")
    n = int(info[0])
    num = int(info[1])

    primes = []
    for i in range(2,2**n):
        if get_factor(i) == None: primes.append(i)
    rang = 2**(n-2)
    count = 0
    for i in range(rang):
        ret = []
        b = ("1{0:0%db}1" % (n - 2)).format(i)
        for base in range(2, 11):
            tmp = int(b, base)
            if tmp in primes: break
            for prime in primes:
                if tmp % prime == 0: ret.append(prime); break 
        if len(ret) != 9: continue
        sys.stdout.write('%s %s\n' % (b, ' '.join([str(x) for x in ret])))
        count += 1
        if count == num: break
