#python 2
import sys


def solve(n):
    digits = set([i for i in xrange(0,10)])
    m = n
    last = None
    asleep = 0
    while(len(digits) > 0):
        if last == m:
            return "INSOMNIA"
        last = m
        s = str(m)
        for i in s:
            if int(i) in digits: digits.remove(int(i))
        asleep += 1    
        if len(digits) == 0: return m
        m = n * (asleep + 1)
    return m



f = open('output.ou', 'w')
fi = open(sys.argv[-1], 'r')
cases = int(fi.readline().strip())
for x in xrange(cases):
    n = int(fi.readline().strip())
    f.write("Case #%i: %s\n" % (x + 1, solve(n)))
f.close()
