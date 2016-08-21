#!/usr/bin/python

def counting(n):
    if n == 0:
        return 'INSOMNIA'

    digits = []
    m = 0
    i = 1
    while len(digits) < 10:
        m = i * n  
        for j in str(m):
            if j not in digits:
                digits.append(j)
        i = i + 1
    return m
    

t = int(raw_input())
for i in xrange(1, t + 1):
    N = int(raw_input())
    result = counting(N)
    print "Case #{}: {}".format(i, result)