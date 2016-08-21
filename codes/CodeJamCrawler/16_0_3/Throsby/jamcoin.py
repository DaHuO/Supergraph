import random
import math

def isprime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def jamCoin(file):

    f = open(file)

    numCases = 0

    seenCoins = []

    chosenCoins = []

    for i, line in enumerate(f):

        if i == 0:
            numCases = int(line)

        else:
            nums = line.split(" ")
            N = int(nums[0])
            J = int(nums[1])

            while len(chosenCoins) < J:
                coin = randGenCoin(N)
                coinString = ""
                for bit in coin:
                    coinString += str(bit)

                if allBasesValid(coin) and coinString not in seenCoins:
                    seenCoins.append(coinString)
                    chosenCoins.append([coinString, findDivisor(base2(coin)), findDivisor(base3(coin)), findDivisor(base4(coin)), findDivisor(base5(coin)), findDivisor(base6(coin)), findDivisor(base7(coin)), findDivisor(base8(coin)), findDivisor(base9(coin)), findDivisor(base10(coin))])

    f.close()

    fp = open("testSmall", 'a')

    iterations = 1
    fp.write("Case #" + str(iterations) + ":\n")
    for lister in chosenCoins:
        fp.write(lister[0] + " " + str(lister[1]) + " " + str(lister[2]) + " " + str(lister[3]) + " " + str(lister[4]) + " " + str(lister[5]) + " " + str(lister[6]) + " " + str(lister[7]) + " " + str(lister[8]) + " " + str(lister[9]) + "\n")

    fp.close()


def findDivisor(num):
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            return x

def randGenCoin(coinLength):
    newCoin = [None]*coinLength
    for i in range(0, coinLength):
        if i == 0 or i == coinLength-1:
            newCoin[i] = 1
        else:
            choice = random.randint(1, 10)
            if choice <= 5:
                newCoin[i] = 0
            else:
                newCoin[i] = 1
    return newCoin

def base2(bits):
    num = 0
    copycat = bits[::-1]
    for i in range(len(copycat)):
        if copycat[i] == 1:
            num += 2**i
    return num

def base3(bits):
    num = 0
    copycat = bits[::-1]
    for i in range(len(copycat)):
        if copycat[i] == 1:
            num += 3**i
    return num

def base4(bits):
    num = 0
    copycat = bits[::-1]
    for i in range(len(copycat)):
        if copycat[i] == 1:
            num += 4**i
    return num

def base5(bits):
    num = 0
    copycat = bits[::-1]
    for i in range(len(copycat)):
        if copycat[i] == 1:
            num += 5**i
    return num

def base6(bits):
    num = 0
    copycat = bits[::-1]
    for i in range(len(copycat)):
        if copycat[i] == 1:
            num += 6**i
    return num

def base7(bits):
    num = 0
    copycat = bits[::-1]
    for i in range(len(copycat)):
        if copycat[i] == 1:
            num += 7**i
    return num

def base8(bits):
    num = 0
    copycat = bits[::-1]
    for i in range(len(copycat)):
        if copycat[i] == 1:
            num += 8**i
    return num

def base9(bits):
    num = 0
    copycat = bits[::-1]
    for i in range(len(copycat)):
        if copycat[i] == 1:
            num += 9**i
    return num

def base10(bits):
    num = 0
    copycat = bits[::-1]
    for i in range(len(copycat)):
        if copycat[i] == 1:
            num += 10**i
    return num

def allBasesValid(bits):
    if isprime(base2(bits)):
        return False
    if isprime(base3(bits)):
        return False
    if isprime(base4(bits)):
        return False
    if isprime(base5(bits)):
        return False
    if isprime(base6(bits)):
        return False
    if isprime(base7(bits)):
        return False
    if isprime(base8(bits)):
        return False
    if isprime(base9(bits)):
        return False
    if isprime(base10(bits)):
        return False
    return True

jamCoin("C-small-attempt3.in")