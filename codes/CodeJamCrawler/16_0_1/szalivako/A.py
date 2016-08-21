'''
Created on 9 Apr 2016

@author: szalivako
'''

def get_digits(n):
    res = []
    while (n > 0):
        res.append(n % 10)
        n //= 10
    return res

def test_number(n):    
    marked = [0 for j in xrange(10)]
    j = 1
    while (True):
        current = n * j
        digits = get_digits(current)
        for di in digits:
            marked[di] = 1
        is_ok = 1
        for t in xrange(10):
            is_ok *= marked[t]
        if (is_ok == 1):
            return current
        j += 1

T = int(raw_input())
for ti in xrange(T):
    n = int(raw_input())
    if (n == 0):
        ans = 'INSOMNIA'
    else:
        ans = str(test_number(n))
        
    print 'Case #' + str(ti + 1) + ': ' + ans