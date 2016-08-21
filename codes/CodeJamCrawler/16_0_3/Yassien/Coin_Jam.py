__author__ = 'Yassien'

def readTestCaseFile(fileName):
    inputLines = []
    cases  =[]
    with open(fileName, 'r') as fp:
        for line in fp:
            number = line.split('\n')
            inputLines.append(number)
        numCases = inputLines[0][0]
        numCases = int(numCases)
        index = 1
        for i in range(numCases):
            line = inputLines[index]
            line = str(line[0])
            numbers = []
            tempNumber = ""
            for ch in line:
                if ch != " ":
                    tempNumber = tempNumber + ch
                else:
                    if tempNumber !=" ":
                        numbers.append(int(tempNumber))
                        tempNumber = ""

            if tempNumber !=" ":
                    numbers.append(int(tempNumber))
            cases.append(numbers)
            index = index + 1
    return  cases

def writeOutput(destDirectory,results):

    fileName = destDirectory+"results.txt"
    filehandle = open(fileName,'w')
    index = 1
    for res in results:
        filehandle.write("Case")
        filehandle.write("\t")
        filehandle.write("#"+str(index)+":")
        filehandle.write("\n")
        coins = res[1]
        for coin in coins:
            jam = coin[0]
            numbers = coin[1]
            filehandle.write(str(jam))
            filehandle.write("\t")
            for num in numbers:
                filehandle.write(str(num))
                filehandle.write("\t")
            filehandle.write("\n")

        index = index + 1

    return
def convertNumIntoDigits(N):
    number = str(N)
    digits = []
    for ch in number:
        if ch != " ":
            digits.append(int(ch))
    return digits
def interpretToNumber(digits,base):
    '''
    number = 0
    index = 0
    for digit in digits:
        number = number + digit*(base**index)
        index = index + 1
        '''
    decimal = 0
    for digit in digits:
        decimal = decimal*base + int(digit)
    return decimal
def factors(n):
    currentDivisor = 1
    done = 0
    while n > 1:
        for i in range(2, int(n) + 1):
            if n % i == 0:
                n /= i
                currentDivisor = i
                done = 1
                break
        if done:
            break
    return currentDivisor
def is_JetCoin(case):
    nonTrivialDivisors = []
    tempConverted = []
    index = 2
    digits = convertNumIntoDigits(case)
    if len(digits)>1:
        if digits[0] ==0 or digits[len(digits)-1] == 0:
            return 0
    ret = 1
    for i in range(9):
        base = index
        print(case)
        #number  = int(case, base)#interpretToNumber(digits,base)
        #digits = convertNumIntoDigits(case)
        #number = interpretToNumber(digits,base)
        number  = int(case, base)
        #print("converted")
        #print(number)
        #print("after factor")
        isPrime = is_prime(number)
        #print("After prime")
        #print(isPrime)
        if  isPrime== 1:
           ret = 0
           break
        else:
            #print("start Factorizing")
            #nonTrivialDivisors.append(factors(number))
            tempConverted.append(number)
            #print("End Factorizing")
        index = index + 1
    if ret  == 1:
        for num in tempConverted:
            nonTrivialDivisors.append(factors(num))
    return ret,nonTrivialDivisors
import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

from random import randint

def generateRandomBit():
    return randint(0,1)

def generateCoinJam(N):
    JamCoinNumber = "1"
    for i in range(N-2):
        JamCoinNumber = JamCoinNumber+ str(generateRandomBit())
    JamCoinNumber = JamCoinNumber+ "1"
    return JamCoinNumber
def solveCoinJamCase(case):
    if len(case) > 1:
        N = case[0]
        J = case[1]
        numSuccessfulCases = 0
        solutions = []
        while numSuccessfulCases<J:
            case = generateCoinJam(N)
            print(case)
            ret,nonTrivialDivisors = is_JetCoin(case)
            if ret == 1:
                print("Jam Coin")
                solutions.append((case,nonTrivialDivisors))
                numSuccessfulCases = numSuccessfulCases + 1
            else:
                print("Not Jam Coin")
    else:
        print("Input Error")

    return solutions
def coinJam(cases,destDirectory):
    if len(cases)> 0 :
        results = []
        for i in range(len(cases)):
            ret = solveCoinJamCase(cases[i])
            results.append((i,ret))
        writeOutput(destDirectory,results)

    return
fileName = "C:/Users/Yassien/Desktop/C-small-attempt0.in"
cases = readTestCaseFile(fileName)
destDirectory = "C:/Users/Yassien/Desktop/"
coinJam(cases,destDirectory)