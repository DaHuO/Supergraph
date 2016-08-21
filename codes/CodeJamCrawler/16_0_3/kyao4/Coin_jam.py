"""
Created on Apr 9, 2016

@author: K.Yao
"""
from math import sqrt, pow


def genCom_real(length, cur_length, digits, numList):
    if cur_length == length:
        numList.append(digits)
        return
    else:
        genCom_real(length, cur_length + 1, digits + "0", numList)
        genCom_real(length, cur_length + 1, digits + "1", numList)


def generateCombination(length):
    numList = []
    cur_length = 0
    genCom_real(length - 2, cur_length, "", numList)
    for i in range(len(numList)):
        numList[i] = "1" + numList[i] + "1"
    return numList


def isPrime(num):
    if num == 1 or num <= 0:
        return False

    i = 0
    sqrtnum = sqrt(num)

    for i in range(2, int(sqrtnum) + 1, 1):
        if num % i == 0:
            return False
    return True


def returnComposite(num):
    if num == 1 or num <= 0:
        return False
    i = 0
    sqrtnum = sqrt(num)
    for i in range(2, int(sqrtnum) + 1, 1):
        if num % i == 0:
            return i
    return False



bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':
    # read input
    with open('input.txt', 'rt') as fin:
        numCases = int(fin.readline())
        caseParams = []
        for i in range(numCases):
            params = fin.readline().strip().split(" ")
            caseParams.append(params)
    outputString = ""
    index = 1
    for i in range(numCases):
        outputString += "Case #" + str(i + 1) + ":" + "\n"
        params = caseParams[i]
        length = int(params[0])
        numCoins = int(params[1])
        numList = generateCombination(length)
        for num in numList:
            num = list(int(digit) for digit in list(num))
            prime_flag = False
            result = 0
            resultList = []
            for base in bases:
                temp_result = 0
                for i in range(len(num)):
                    numR = list(num)
                    numR.reverse()
                    temp_result += numR[i] * pow(base, i)
                if isPrime(temp_result):
                    prime_flag = True
                    resultList.clear()
                    break
                else:
                    resultList.append(temp_result)
            if not prime_flag:
                outputString += "".join(str(digit) for digit in list(num)) + " "
                # print(resultList, end="")
                for numDiffBases in resultList:
                    outputString += str(returnComposite(numDiffBases)) + " "
                outputString += "\n"
                index += 1
                if index - 1 == numCoins:
                    break
    fout = open('output.txt', 'wt', encoding='utf-8')
    fout.write(outputString)
    fout.close()

