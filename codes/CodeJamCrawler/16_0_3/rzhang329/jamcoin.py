import sys
import math

def generateCoins(coinSize, coinsNeeded):
    num = 0
    coins = []
    while len(coins) < coinsNeeded:
        gen = bin(num)[2:]
        middle = "{0:0{1}}".format(int(gen),coinSize-2)
        binary = "1{0}1".format(middle)
        divisors = getDivisors(tuple(int(x) for x in binary[::-1]))
        if divisors is not None:
            result = [binary]
            result += [str(x) for x in divisors]
            coins.append(tuple(result))
        num += 1
    return tuple(coins)

def getDivisors(reversedDigits):
    result = []
    for base in range(2, 11):
        div = getDiv(reversedDigits, base)
        if div is None:
            return None
        else:
            result.append(div)
    return result

"""
Uses function sqrt from standard python library math
"""
def getDiv(reversedDigits, base):
    num = sum(base**i for i,x in enumerate(reversedDigits) if x>0)
    div = 2
    while div <= int(math.sqrt(num)):
        if (num % div) == 0:
            return div
        div += 1
    return None

if __name__ == '__main__':
    inputFile = open(sys.argv[1], 'r')
    inputData = inputFile.read().splitlines()[1].split(' ')
    coinSize = int(inputData[0])
    coinsNeeded = int(inputData[1])
    outputData = generateCoins(coinSize, coinsNeeded)
    outputFile = open("output.txt", 'w')
    outputFile.write("Case #1:\n")
    for item in outputData:
        outputFile.write("{0}\n".format(' '.join(item)))
    inputFile.close()
    outputFile.close()
