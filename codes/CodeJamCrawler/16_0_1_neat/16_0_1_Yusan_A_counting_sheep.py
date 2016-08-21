#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2015 qualification round
A: counting sheep
'''

def last_number(N):
    if N <= 0:
        return 'INSOMNIA'
    seen = {}
    number = N
    while len(seen) < 10:
        digits = str(number)
        for d in digits:
            seen[d] = True
        number += N
    return number - N


T = int(raw_input())
for case_number in range(1, T + 1):
    N = int(raw_input())
    print 'Case #%d: %s' % (case_number, last_number(N))
