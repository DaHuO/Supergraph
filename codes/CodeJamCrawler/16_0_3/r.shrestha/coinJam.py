import sys
from math import sqrt

def checkPrime(number):
    if number <= 1:
        return False, 0
    elif number == 2:
        return True, 0
    elif number & 1 == 0:
        return False, 2
    else:
        isPrime = True
        nonTrivialDivisor = 0
        i = 3
        while i < long(sqrt(number)) + 1:#for i in xrange(3, long(sqrt(number)) + 1, 2):
            if number % i == 0:
                isPrime = False
                nonTrivialDivisor = i
                break
            i += 2
        return isPrime , nonTrivialDivisor

class CoinString:
    '''
    This class is iterator for coin string of certain length N
    The string may not be a valid jam coin string (doesn't check the prime part)
    '''
    def __init__(self, N):
        self.N = N
        
        self.varString = ''
        self.varStringIndex = long(0)
        # combinations of the string between the start and end 1s
        self.varStringCombinations = long(2) ** (N - 2)

    def __iter__(self):
        return self

    def generateVarString(self):
        number = self.varStringIndex
        string = ''
        for i in range(self.N-2):
            bit = number & 1
            string += str(bit)
            number >>= 1
        self.varStringIndex += 1
        return string

    def next(self):
        if self.varStringIndex >= self.varStringCombinations:
            raise StopIteration
        else:
            return '1' + self.generateVarString() + '1'

def checkValid(string):
    isValid = True

    bases = range(2, 11) # 2 to 10
    nonTrivialDivisors = []
    for base in bases:
        number = long(string, base)
        isPrime, nonTrivialDivisor = checkPrime(number)
        if isPrime: 
            isValid = False
            break
        else:
            nonTrivialDivisors.append(nonTrivialDivisor)
    return isValid, nonTrivialDivisors

# debug
# N = int(sys.argv[2])
# coinStrings = CoinString(N)
# print 'Number: ', N
# for coinString in coinStrings:
#     isValid, nonTrivialDivisors = checkValid(coinString)
#     if isValid:
#         print '%s %s' % (coinString, ' '.join([str(i) for i in nonTrivialDivisors]))
            

# debug
# coinStrings = CoinString(6)
# for string in coinStrings:
#     isValid, nonTrivialDivisors = checkValid(string)
#     if isValid:
#         print string, nonTrivialDivisors, [int(string, base) for base in range(2, 11)]

# main script starts

with open(sys.argv[1]) as f:
    content = f.read().splitlines()

with open('io/coinJam.out', 'w') as f:
    T = int(content[0])
    for caseIndex in range(1, T+1):
        N, J = content[caseIndex].split(' ')
        N = int(N); J = int(J)

        coinStrings = CoinString(N)
        coinCount = 0

        print 'Case #%d:' % (caseIndex)
        f.write('Case #%d:\n' % (caseIndex))
        while coinCount < J:
            coinString = coinStrings.next()
            isValid, nonTrivialDivisors = checkValid(coinString)
            if isValid:
                print '%s %s, nums:%s' % (coinString, ' '.join([str(i) for i in nonTrivialDivisors]), ' '.join([str(long(coinString, base)) for base in range(2, 11)]))
                f.write('%s %s\n' % (coinString, ' '.join([str(i) for i in nonTrivialDivisors])))
                coinCount += 1

