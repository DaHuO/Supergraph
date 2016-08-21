from itertools import product
from math import sqrt
pro = product

t = 1
print "Case #1:"

def is_prime(x):
    divisor = 2
    while divisor <= sqrt(x):
        if x % divisor == 0:
            return [False, divisor]
        divisor += 1
    return [True, -1]

def notprime(num):
    divs = []
    for i in range(2, 11):
        n = 0
        for j in range(len(num)):
            n += i**(len(num)-j-1)*int(num[j])
        ev, div = is_prime(n)
        divs.append(div)
        if ev:
            return [False, -1]
            break
    return [True, divs] 
            
n, j = 16, 50

count = 0
nums = pro("01", repeat = n-2)
for i in nums:
    ev2, divs = notprime("1" + "".join(i) + "1")
    if ev2:
        count += 1
        print "1" + "".join(i) + "1" + " " + " ".join(map(str, divs))
    if count == j:
        break
