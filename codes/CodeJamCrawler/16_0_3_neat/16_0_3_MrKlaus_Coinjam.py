def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

import itertools

def kbits(n, k):
    result = []
    for bits in itertools.combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        result.append(''.join(s))
    return result

def convertNumber(D,baseNum):
    return int(D, base=baseNum)

def generateBaseNumList(pjcString):
    bnList = []
    for i in range(2,11):
        N = convertNumber(pjcString,i)
        bnList.append(N)

    return bnList

def checkNoPrimes(bnl):
    for k in range(len(bnl)):
        if is_prime(bnl[k]):
            return False
            break

    return True

def generateDivisor(num):
    i = 2
    while i < num:
        if num % i == 0:
            return i
        i = i + 1

def generateDivisorList(bnl):
    dList = []
    for i in range(len(bnl)):
        dList.append(generateDivisor(bnl[i]))

    return dList

def generateJamCoins(N,J):
    fourteenList = kbits(N-2,7)
    sixteenList = []

    for i in range(len(fourteenList)):
        testNum = '1' + fourteenList[i] +'1'
        sixteenList.append(testNum)


    #Try the 16-digit numbers in the list
    jcList = []
    jcBNList =[]
    for i in range(len(sixteenList)):
        jcString = sixteenList[i]
        BNList = generateBaseNumList(jcString)
        if checkNoPrimes(BNList):
            jcList.append(jcString)
            jcBNList.append(BNList)

        if len(jcList) == J:
            break


    JCoutputList = []
    for i in range(len(jcList)):
        jc = jcList[i]
        BNList = jcBNList[i]
        jcDList = generateDivisorList(BNList)

        JCoutputList.append(str(jc) + " " + (" ".join(str(x) for x in jcDList)))

    return JCoutputList


BSmallFile = 'C-small-attempt0.in'

f = open(BSmallFile, 'r')
T = int(f.readline())

o = open('C-small-output.txt','w')

for j in range(T):
    N = 16
    J = 50
    L = generateJamCoins(N,J)
    o.write("Case #1:" + '\n')
    for i in range(len(L)):
        o.write(L[i] + '\n')

f.close()
o.close()





