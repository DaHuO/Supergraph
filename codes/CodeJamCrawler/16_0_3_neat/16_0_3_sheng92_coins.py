from math import sqrt; from itertools import count, islice
input = '''1
32 500
'''

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(min(sqrt(n)-1,2147483647))))

def getFactor(n):
    maxI = int(min(sqrt(n)-1,5000))
    for i in islice(count(2), maxI):
        if n%i == 0:
            return i
    return -1

def convBase(bin, n):
    j = 0
    for i in bin:
        j *= n
        j += int(i)
    return j

def coingen(n, j):
    count = 0
    curr = 0
    while count < j:
        test = '1' + "{0:b}".format(curr).zfill(n-2) + '1'
        works = True
        factors = [0] * 9
        for i in range(2,11):
            convI = convBase(test, i)
            factors[i-2] = getFactor(convI)
            if factors[i-2] == -1:
                works = False
                break
        curr += 1
        if works:
            count += 1
            print test + ' ' +  ' '.join(map(str,factors))

split = input.splitlines()
for i in range(1, int(split[0])+1):
    print 'Case #%i: ' % i
    coingen(*tuple([int(j) for j in split[i].split()]))