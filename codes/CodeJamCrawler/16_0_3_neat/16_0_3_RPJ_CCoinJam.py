import time

def isPrimeNumber(number):
    pos = 2
    start = time.time()
    while number != pos:
        if (number % pos) == 0:
            return False, pos
        pos += 1

        if time.time() - start > .1:
            break
    return True, number

def coinLargeJam():
    N = 32
    startBin = 0b10000000000000000000000000000001
    countPrimes = 0
    M = 500
    STEP = 5

    outFile = open(r'C:\Users\Remi\Code\Data\C_small.out', 'w')
    outFile.write('Case #1:\n')
    while countPrimes < M:
        res, divs = [], []
        binStr = str(bin(startBin))[2:]
        if binStr[0] != '1' or binStr[-1] != '1':
            startBin += STEP
            continue
        for base in range(2, 11):
            num = int(binStr, base)
            isPrime, div = isPrimeNumber(num)
            res.append(isPrime)
            divs.append(str(div))
        if not any(res):
            outFile.write('%s %s\n' % (binStr, ' '.join(divs)))
            countPrimes += 1
        startBin += STEP

    outFile.close()

def coinSmallJam():
    N = 16
    startBin = 0b1000000000000001
    countPrimes = 0
    M = 50
    STEP = 5

    outFile = open(r'C:\Users\Remi\Code\Data\C_small.out', 'w')
    outFile.write('Case #1:\n')
    while countPrimes < M:
        res, divs = [], []
        binStr = str(bin(startBin))[2:]
        if binStr[0] != '1' or binStr[-1] != '1':
            startBin += STEP
            continue
        for base in range(2, 11):
            num = int(binStr, base)
            isPrime, div = isPrimeNumber(num)
            res.append(isPrime)
            divs.append(str(div))
        if not any(res):
            outFile.write('%s %s\n' % (binStr, ' '.join(divs)))
            countPrimes += 1
        startBin += STEP

    outFile.close()

#coinSmallJam()
coinLargeJam()