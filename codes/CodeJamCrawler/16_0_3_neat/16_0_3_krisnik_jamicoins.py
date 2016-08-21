# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math

def getTrivialDivisorsString(listOfNumbers):
    result = str(listOfNumbers[0])
    for i in range(1, len(listOfNumbers)):
        result = result + " " + str(listOfNumbers[i])

    return result

def checkTrivialDivisor(number):

    limit = int(math.sqrt(number))
    for i in range(2,limit + 1):
        if number % i == 0:
            return i

    return -1

def isPrime(number):
    limit = int(math.sqrt(number))
    for i in range(2,limit + 1):
        if number % i == 0:
            return False

    return True
    pass

#number should be string, base should be number
def convertToBase(number, base):
    output = 0
    lengthNumber = len(number)
    for i in range(lengthNumber):
        output += int(number[i]) * math.pow(base, lengthNumber - i - 1)

    return int(output)
    pass

def normalize(number, maxLength):
    if len(number) == maxLength:
        return number
    else:
        diff = maxLength - len(number)
        zeroes = ""
        for z in range(diff):
            zeroes += "0"
        number = zeroes + number
        return number
    pass

t = int(raw_input())  # read a line with a single integer
for testCase in xrange(1, t + 1):
    print "Case #{}:".format(testCase)
    n, jamis = [int(s) for s in raw_input().split(" ")]
    #ok. 1 and n are ignored and i keep it one.
    maxNum = int(math.pow(2, n-2))
    jamiCount = 0

    for k in range(maxNum):
        # i will have binary represnetaion of number in between 1 and 1
        binRep = normalize(bin(k)[2:], n-2)
        inputForTest = "1" + binRep + "1"
        listOfJamiCons = []
        isJamiCoin = True
        for l in range(2,11):
            convertedToBase = convertToBase(inputForTest, l)
            if isPrime(convertedToBase):
                isJamiCoin = False
                break
            else:
                listOfJamiCons.append(convertedToBase)
        if isJamiCoin:
            # print trivial divisors.
            jamiCount += 1
            trivialDivisors = []
            for jam in listOfJamiCons:
                trivDivisor = checkTrivialDivisor(jam)
                trivialDivisors.append(trivDivisor)

            divisorsString = getTrivialDivisorsString(trivialDivisors)
            print "{} {}".format(inputForTest, divisorsString)

        if jamiCount == jamis:
            break
            #Case #1:
            #100011 5 13 147 31 43 1121 73 77 629
