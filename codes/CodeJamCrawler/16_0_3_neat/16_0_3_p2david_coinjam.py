import functools
import math
import itertools
size =  "large"

def solve(length, count):
    sol = list()
    prod = itertools.product(['0', '1'], repeat=length -2)
    for x in prod:
        num_str = ''.join(['1'] + list(x) + ['1'])
        _10based = to_10based(num_str)
        print("10based", _10based) 
        legit =is_jamcoin(_10based)

        if legit:
            divisors = find_divisors(_10based)
            print(num_str, legit, divisors)
            sol.append((num_str, divisors))
            if len(sol) == count:
                return sol
    return sol

def find_divisors(nums):
    result = list()
    for n in nums:
        result.append(divisor(n))
    return result

def to_10based(num_str):
    return [int(num_str, b) for b in range(2,11)] 

def is_jamcoin(_10based):
    for num in _10based:
        if is_prime(num):
            return False
    return True

def divisor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            return i
    if n > 1:
        return n 

def is_prime(number):
    if number == 2:
       return true
    if number % 2 == 0:
        return False
    
    i = 3
    sqrtOfNumber = math.sqrt(number)

    limit = 10000
    cnt = 0
    
    while i <= sqrtOfNumber:
        if number % i == 0:
            return False
        i = i+2
        cnt = cnt + 1
        if (cnt > limit): #shortcut, ignore it
            return True
        
    return True

f = open('C-%s.in' % size)
o = open('C-%s.out' % size, 'w')
n = int(f.readline())
line2 = f.readline().split()
length = int(line2[0])
count = int(line2[1])
print(length, count)
sol = solve(length, count)
o.write("Case #%d:\n" % (1))
for s in sol:
    o.write("%s %s\n" % (s[0], ' '.join(map(str, s[1]))))
f.close()
o.close()
