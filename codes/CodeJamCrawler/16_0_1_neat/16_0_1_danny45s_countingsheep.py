import numpy as np
import sys
a=open(sys.argv[-1]).readlines()[1:]

def solve(i):
    if i == 0:
        return 'INSOMNIA'
    used = np.zeros(10)
    mult = 1
    while 0 in used:
        a = i * mult
        while a != 0:
            used[a % 10] = 1
            a /= 10
        mult += 1
    return i * (mult - 1)

for i in range(len(a)):
    print 'Case #' + str(i + 1) + ': ' + str(solve(int(a[i])))
