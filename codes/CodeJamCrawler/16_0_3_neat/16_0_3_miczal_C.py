

primes = dict()
cache = list()

import math

for i in range(8):
    cache.append(list())
    for j in range(16):
        cache[i].append((i+3)**j)#math.pow(i+3, j))

#print(cache)

def isPrime(val):
    try:
        result = primes[val]
        return result
    except KeyError:
        result = computePrime(val)
        primes[val] = result
        return result

def computePrime(val):
    if val % 2 == 0:
        #print(val)
        #print("EVEN")
        return False
    i = 2
    while i*i < val:
        if val % i == 0 :
            return False
        i += 1
    return True

def getDivisors(val):
    for i in range(2, val):
        if (val % i) != 0:
            continue
        return i

def nextDivisor(start, val):
    for i in range(start+1, val):
        if (val % i) != 0:
            continue
        return i
    return None

def representation(base, i_bin):
    result = 0

    for x in range(len(i_bin)-1,-1,-1):

        if i_bin[x] == '1':
            result+=cache[base-3][len(i_bin)-1-x]
    return result


T = int(input()) #always 1
for t in range(T):
    [N, J] = [int(i) for i in input().split(' ')]

    def solver():
        result = []

        start = 2**(N-1) + 1
        limit = 2**N - 1

        for i in range(start, limit + 1):
            get_out = False
            if i%2==0:
                continue
            values = list()
            if isPrime(i):
                continue
            values.append(i)
            i_bin = bin(i)[2:]
            for j in range(3, 11):
                r = representation(j, i_bin)
                if isPrime(r):

                    get_out = True
                    break
                else:
                    values.append(r)
            if get_out:
                continue
            divisors = list()
            for x in range(9):
                divisor = getDivisors(values[x])
                while divisor in values:
                    divisor = nextDivisor(divisor, x)
                    if divisor is None:
                        get_out = True
                        break
                if get_out:
                    break
                divisors.append(divisor)
            if get_out:
                    continue
            partial = i_bin
            for divisor in divisors:
                partial += " " + str(divisor)
            result.append(partial)
            if len(result) == J:
                return result
        return result

    result = solver()
    print("Case #1:")
    for res in result:
        print(res)

#    coins = [None] * J
#    divisors = [None] * 9 # <2;10>
    
    #print("Case #" + str(t+1) + ": " + str(changes))

