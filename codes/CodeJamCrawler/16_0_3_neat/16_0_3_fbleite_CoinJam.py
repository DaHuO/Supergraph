__author__ = 'fbleite'

import multiprocessing
import math
from itertools import islice, count
from PerformanceMeasure import PerformanceMeasure
import functools

def printOutput (outputSet) :
    print(outputSet)
    print('Case #1:')
    for key, value in outputSet.items():
        print('{} {}'.format(key, ''.join(str(ntd) + ' ' for ntd in value)))

#
def isPrime(n, isprime):
    if n == 2:
        isprime.value = True
        return True
    if n % 2 == 0 or n <= 1:
        isprime.value = False
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            isprime.value = False
            return False
    isprime.value = True
    return True

# def isPrime(n, isprime):
#     if n < 2: return False
#     for number in islice(count(2), int(math.sqrt(n)-1)):
#         if not n%number:
#             isprime.value = False
#             return False
#     isprime.value = True
#     return True


def getAllBases(original):
    allBases = []
    for i in range(2, 11):
        allBases.append(int(original, i))
    return allBases

def addOneReturnNewString(bitString):
    newInt = int(bitString, base=2) + 1
    newBitString = str(bin(newInt))[2:]
    for i in range(len(bitString) - len(newBitString)):
        newBitString = ('0' * (len(bitString) - len(newBitString))) + newBitString
    return newBitString

def isNumberPrimeAnyBase(number):
    allBases = getAllBases(number)
    for oneBase in allBases:
        # print('Is it prime: ' + str(oneBase))
        isprime = multiprocessing.Value('b', False)
        p = multiprocessing.Process(target=isPrime, args=(oneBase, isprime))
        p.start()
        p.join(10)
        if p.is_alive():
            p.terminate()
            print('Gave up')
            isprime.value = True
            p.join()
        if isprime.value:
            return True

    return False

def firstFactor(n):
    for i in range(2, int(n*0.5) + 1) :
        if n % i == 0:
            return i;
    raise OverflowError('No factor found for n:' + str(n) + ' and i: ' + str(i))


def getNonTrivialDivisors(number):
    print('Finding non trivial in coin: ', number)
    allBases = getAllBases(number)
    nonTrivial = []
    for base in allBases:
        print('Base number: ', str(base))
        possibleNonTrivial = firstFactor(base)
        print('Added non trivial: ', possibleNonTrivial)
        nonTrivial.append(possibleNonTrivial)
    return nonTrivial

def createCoins(numberOfCoins, sizeOfCoin):
    listOfCoins = []
    innerCoin = '0' * (sizeOfCoin - 2)
    while (len(listOfCoins) < numberOfCoins) and len(innerCoin) == (sizeOfCoin -2):
        potentialCoin = '1' + innerCoin + '1'
        print('potentialCoin: ' + potentialCoin)
        if isNumberPrimeAnyBase(potentialCoin):
            innerCoin = addOneReturnNewString(innerCoin)
        else :
            listOfCoins.append(potentialCoin)
            print('Number of created coins: ' + str(len(listOfCoins)))
            innerCoin = addOneReturnNewString(innerCoin)
    return listOfCoins

def solveProblem(line):
    finalSet = {}
    sizeOfCoin, numberOfCoins = line.split(' ')
    jamCoins = createCoins(int(numberOfCoins), int(sizeOfCoin))
    for jamCoin in jamCoins:
        finalSet[jamCoin] = getNonTrivialDivisors(jamCoin)
        print('Number of verified coins:', str(len(finalSet)))
    return finalSet


def CoinJam():
    testFile = open("/Users/fbleite/Development/CodeJam/CoinJam/SampleCoin", "r")
    line1 = False
    numberOfCases = 0
    finalSet = []

    for line in testFile:
        if (not line1):
            line1=True
            numberOfCases = int(line)
        else :
            printOutput(solveProblem(line.replace('\r', '').replace('\n', '')))

# CoinJam()


def testCreateCoinsSmall():
    print(createCoins(50, 16))
def testCreateCoinsLarge():
    coins = createCoins(500, 32)
    print(coins)
    print(len(coins))

def testSingleNumber():
    # p = multiprocessing.Process(target=isPrime, args=(1326443518324400147398873,))
    isprime = multiprocessing.Value('b', False)
    print(isprime.value)
    p = multiprocessing.Process(target=isPrime, args=(1326443518324400147398873, isprime))
    p.start()
    p.join(10)
    print(isprime.value)
    if p.is_alive():
        p.terminate()
        p.join()



# print(getNonTrivialDivisors('1000000010001001'))

perf = PerformanceMeasure(CoinJam)
perf.runFuntionAndCheckPerformance()
# perf2 = PerformanceMeasure(testCreateCoinsLarge)
# perf2.runFuntionAndCheckPerformance()
