import numpy as np
import sys
a=open(sys.argv[-1]).readlines()[1:]


def solve(k, c, s):
    ans = ''
    for i in range(1, k + 1):
        ans += str(i) + ' '
    return ans


for i in range(len(a)):
    kcs = a[i].split()
    k = int(kcs[0])
    c = int(kcs[1])
    s = int(kcs[2])
    print 'Case #' + str(i + 1) + ': ' + solve(k, c, s)
