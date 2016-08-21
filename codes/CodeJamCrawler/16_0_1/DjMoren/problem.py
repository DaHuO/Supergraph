'''
Created on Apr 9, 2016

@author: hduser
'''

import re


def solve(n):
    if (n == 0):
        return 'INSOMNIA'
    else:
        needed = set(str(x) for x in range(0, 10))
        counted = set(re.findall('\d', str(n)))
        k = 1
        last = n
        while (counted != needed):
            k += 1
            last = k * n
            counted |= set(re.findall('\d', str(last)))
        return last


t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, solve(n))
