#!/usr/bin/python

from sys import stdin, stdout

T = int(stdin.readline().strip())

for case_num in range(1, T+1):
    N = int(stdin.readline().strip())
    if N == 0:
        answer = 'INSOMNIA'
    else:
        k = 1
        digits = {0,1,2,3,4,5,6,7,8,9}
        while digits:
            kN = k * N
            kN_digits = [ int(c) for c in str(kN) ]
            for d in kN_digits:
                digits.discard(d)
            k += 1
        answer = str(kN)
    stdout.write("Case #{:d}: {:s}\n".format(case_num, answer))
