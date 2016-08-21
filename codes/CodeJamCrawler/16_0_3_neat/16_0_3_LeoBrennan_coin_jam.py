import sys
from math import sqrt, pow, cos
from itertools import count, islice

name = "C-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def coinJam():
    for testCase in range(1, testCases + 1):
        line = input().split()
        N = int(line[0])
        J = int(line[1])
        print("Case #" + str(testCase) + ": ")
        solutionsFound = 0
        numberToTest = 1;
        binaryAnswers = list()
        while solutionsFound < J:
            testingBinary = bin(numberToTest).zfill(N)
            newList = list(testingBinary)
            while len(newList) > N:
                del newList[0]
            newList[0] = '1'
            newList[len(newList)-1] = '1'
            for index in range(1, len(newList)):
                if (newList[index] == 'b'):
                    newList[index] = '0'
            finalBinary = ''.join(newList)
            i = 2
            completed = False
            finalNumbers = list()
            finalNumbers.append(finalBinary)
            while not completed:
                numberToCheck = int (finalBinary, i)
                checkedForPrime = isPrime(numberToCheck)
                if not checkedForPrime == 0:
                    finalNumbers.append(checkedForPrime)
                    if (i is 10):
                        completed = True
                else:
                    completed = True
                i += 1
            if len(finalNumbers) is 10:
                if not finalNumbers[0] in binaryAnswers:
                    solutionsFound += 1
                    binaryAnswers.append(finalNumbers[0])
                    print (str(finalNumbers[0]) + " " + str(finalNumbers[1]) + " " + str(finalNumbers[2]) + " " + str(finalNumbers[3]) + " " + str(finalNumbers[4]) + " " + str(finalNumbers[5]) + " " + str(finalNumbers[6]) + " " + str(finalNumbers[7]) + " " + str(finalNumbers[8]) + " " + str(finalNumbers[9]))
            numberToTest += 2


def isPrime(n):
    if n < 2: return False
    cubeRootNumber = sqrt(n)
    if (n > 1000000000000000000000000000000):
        cubeRootNumber = eval(n, 5.0)
    elif (n > 1000000000000000000000000):
        cubeRootNumber = eval(n, 4.0)
    elif (n > 100000000000000):
        cubeRootNumber = eval(n, 3.0)
    for number in islice(count(2), int(cubeRootNumber-1)):
        if not n%number:
            return number
    return 0

def eval( i, j ):
    return i**(1./j)

coinJam()