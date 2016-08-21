#!/usr/bin/env python

def getPrimes(upper):
    numbers = set(range(upper, 1, -1)) # all the elements < upper
    primes = []
    while numbers: # until the queue is empty
        prime = numbers.pop() # take the largest, add to primes
        primes.append(prime)
        numbers.difference_update(set(range(prime*2, upper+1, prime)))
    return primes

def getNextMid(middle):
    carry = True
    midlist = list(middle)
    for i in range(len(midlist)-1, -1, -1):
        if(carry and midlist[i] == "1"):
            midlist[i] = "0"
        elif(carry and midlist[i] == "0"):
            midlist[i] = "1"
            carry = False

    return ''.join(midlist)


def smallestDivisor(number, primeList):
    for i in range(0, len(primeList) - 1):
        if(number % primeList[i] == 0):
            return primeList[i]
    return -1


def getListString(thelist):
    returnstring = ""
    for i in range(len(thelist)):
        returnstring += str(thelist[i]) + " "

    return returnstring.strip()


N = 32
J = 500

jams = []       # keep track of the jam coins we find
num_found = 0

start = "1"
end = "1"
middle = "0"*(N-2)

primes = getPrimes(2**(N/2)) # get all the primes < 2**N

trial = 0
while(trial < 2**N and num_found < J):
    
    possible = start + middle + end
    divisors = []
    Prime = False
	
    for base in range(2, 11):
        k = int(possible, base)
        #if(k not in composites): # a new number
        d = smallestDivisor(k, primes)
        if(d > 0 and k%d == 0 and k != d): # k is composite
            divisors.append(d)
        else:
            Prime = True
            break
        
    if(not Prime):
        jams.append([possible, divisors])
        num_found += 1
        
    middle = getNextMid(middle)
    trial += 1

i = 0
print("Case #1:")
for i in range(len(jams)):
    jam = jams[i][0]
    divisors = jams[i][1]
    line = "{} {}".format(jam, getListString(divisors))
    print(line)
             
        
