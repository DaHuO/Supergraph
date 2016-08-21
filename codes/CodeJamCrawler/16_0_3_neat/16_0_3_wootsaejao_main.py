from multiprocessing import Pool
import os
import sys
import math
import random

def debug(*args):
    if os.environ.get('DEBUG'):
        print(*args)

def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

assert isPrime(9) == False
assert isPrime(28) == False
assert isPrime(65) == False
assert isPrime(126) == False
assert isPrime(217) == False
assert isPrime(334) == False
assert isPrime(337) == True

def splitTextCharInt(text):
    lst = []
    for c in text:
        lst.append(int(c))
    return lst

assert splitTextCharInt('1234') == [1,2,3,4]

def baseToDecimal(base, zerosAndOnesStr):
    lst = splitTextCharInt(zerosAndOnesStr)
    result = 0
    for power, i in enumerate(reversed(lst)):
        result += i * base ** power
    return result

assert baseToDecimal(3, '110111') == 337

def getNontrivialDivisor(n):
    for i in range(2, n):
        if n % i == 0:
            return i

assert getNontrivialDivisor(9) == 3
assert getNontrivialDivisor(217) == 7

def genCoin(length):
    result = '1'
    for _ in range(length-2):
        result += random.choice(['0', '1'])
    result += '1'
    return result

assert len( genCoin(5) ) == 5

ValidCoin = []
InvalidCoin = []

def genJamcoin(length):
    global InvalidCoin
    global ValidCoin
    while True:
    # for _ in range(10):
        fail = False
        coin = genCoin(length)
        if coin in InvalidCoin or coin in ValidCoin:
            debug('same coin')
            continue
        debug('coin:', coin)
        divisors = []
        for base in range(2, 11):
            dec = baseToDecimal(base, coin)
            if isPrime(dec):
                InvalidCoin.append(coin)
                fail = True
                debug(coin, base, 'prime')
                break
            divisors.append(getNontrivialDivisor(dec))
        if not fail:
            ValidCoin.append(coin)
            break

    return '{} {}'.format(
        coin,
        ' '.join(map(str, divisors)),
    )

INPUT_LINES = 1  # number of input lines per case

if __name__ == '__main__':
    totalCases = int( input() )

    # extract arguments
    caseArgsList = []
    for _ in range(totalCases):
        args = []
        for _ in range(INPUT_LINES):
            args.append(input())
        caseArgsList.append(args)

    txt = caseArgsList[0][0]
    argsList = txt.split()
    length = int( argsList[0] )
    amount = int( argsList[1] )
    debug(length, amount)

    print('Case #1:')

    # solve
    with Pool() as p:
        # results = map(genJamcoin, [length for _ in range(amount)])
        results = p.map(genJamcoin, [length for _ in range(amount)])
        for res in results:
            print(res)
