'''
Created on 9 Apr 2016

@author: szalivako
'''

def next_state(current):
    i = 0
    while (current[i] == 1):
        current[i] = 0
        i += 1
    current[i] = 1
    
    return current

def transform(num, base):
    res = 0
    
    num = num[::-1]
    digit = 1
    for ni in num:
        res += digit * ni
        digit *= base
    
    return res

def findDivisor(n):
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            return i
        i += 1
    return -1

cnt = 0

state = [0 for i in xrange(14)]

print 'Case #1: '

for i in xrange(2 ** 14):
    current = [1] + state + [1]
    divisors = []
    is_found = True
    for base in xrange(2, 11):
        number = transform(current, base)
        d = findDivisor(number)
        if (d == -1):
            is_found = False
            break
        else:
            is_found = True
            divisors.append(d)
    
    if (is_found):
        cnt += 1
        jamCoin = ''
        for ci in current:
            jamCoin += str(ci)
        print jamCoin, 
        for di in divisors:
            print di,
        print
        
        if (cnt == 50):
            break
    
    state = next_state(state)
        