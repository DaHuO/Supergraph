from sys import stdin
import re

T = int(stdin.readline())

for case in xrange(1,T+1):
    N = int(stdin.readline().strip())
    if N == 0:
        result = 'INSOMNIA'
    else:
        digits = [False] * 10
        i = 0
        while not all(digits):
            i += 1
            number = i * N
            strdigits = str(number)
            for digit in strdigits:
                digits[int(digit)] = True
        result = N * i

    print 'Case #{0}: {1}'.format(case, result)

