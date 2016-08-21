from math import sqrt

t = raw_input();
data = raw_input();
primes = [-1] * (10**8 + 5)
 
for i in range(2, 10**8 + 2):
    if primes[i] != -1:
        continue
    p = 2 * i
    while( p <= 10**8 + 4 ):
        if(primes[p] == -1):
            primes[p] = i
        p += i

primeNums = []
for i in range(2, 10**8 + 2):
    if(primes[i] == -1):
        primeNums.append(i)
        #print i


storedData = {}
def primalityCheck(n):
    if n <= 10 ** 8:
        return primes[n]
    if n in storedData:
        return storedData[n]
    
    end = int(sqrt(n))

    for num in primeNums:
        if num > end:
            break
        if n % num == 0:
            storedData[n] = num
            return num
    storedData[n] = -1
    return -1

 
j = 50
n = 16

smallest = (2 ** (n - 1)) + 1
largest = (2 ** n) - 1

count = 0
outputs = []

for k in range(smallest, largest + 1, 2):
    binStr = "{0:b}".format(k)
    divisors = [binStr]
    for base in range(2, 11):
        val = int(binStr, base)
        divisor = primalityCheck(val)
        if(divisor == -1):
            break
        divisors.append(str(divisor))
    if(len(divisors) == 10):
        outputs.append(divisors)
        count += 1
    if(count == j):
        break


print "Case #1:"
for output in outputs:
    print " ".join(output)
