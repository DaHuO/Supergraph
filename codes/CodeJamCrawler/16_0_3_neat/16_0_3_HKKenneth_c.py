import sys
import math
import resource
#import objgraph


rsrc = resource.RLIMIT_DATA
soft, hard = resource.getrlimit(rsrc)
#resource.setrlimit(rsrc, (102400, hard))

def find_factor(num):
    for d in range(2, 100000):
        if num % d == 0 and d != num:
            return d
    return -1


def get_list(num, list_):
    s = "{0:b}".format(num)
    list_.append(s)
    for b in range(2,11):
        target = int(s, b)
        fac = find_factor(target)
        if fac == -1:
            break
        else:
            list_.append(str(fac))


t = None
#cache = {}
count = 0
for line in sys.stdin:
    if t is None:
        t = int(line)
        print "Case #1:"
        continue
    n, j = (int(i) for i in line.split(' '))
    base = int(math.pow(2, n-1)) + 1
    while count < j:
        factors = []
        get_list(base, factors)
        base += 2
        if len(factors) == 10:
            print " ".join(factors)
            count += 1
        del factors 
