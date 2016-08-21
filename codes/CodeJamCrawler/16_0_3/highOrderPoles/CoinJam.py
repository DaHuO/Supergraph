import numpy as np

class CoinJam:
    def readLimits(self):
        # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
        # This is all you need for most Google Code Jam problems.
        self.cases = []
        self.numCases = 0

        self.numCases = int(raw_input())  # read a line with a single integer
        self.cases = [int(s) for s in raw_input().split(" ")]

    def printOne(self, results):
        print "Case #1:"
        for i in xrange(len(results)):
            jamCoin, divisors = results[i]
            print jamCoin, divisors

    def run(self):
        self.readLimits()
        size, requiredCases = self.cases

        if size <= 16:
            self.results = self.process(self.cases)
        else:
            self.results = self.specialTwos(requiredCases)
            # case4 = self.findAll(4)
            # case8 = self.findAll(8)

        self.printOne(self.results)

    # def findAll(self, size):
    #     cases = size, np.power(4, size)
    #     result = self.process(cases)

    #     print len(result)

    def specialTwos(self, size):
        baseArrays = self.getBaseArrays(2)
        twoBitSums = [sum(baseArray) for baseArray in baseArrays]
        results = []

        generatedJams = 0

        while generatedJams < size:
            halfVector = self.getMidCoinBool(generatedJams, 14)
            vector = [0] * (2 * len(halfVector))
            vector[::2] = halfVector
            vector[1::2] = halfVector
            jamCoin = [1, 1] + vector + [1, 1]
            generatedJams += 1

            jamString = ''.join([str(i) for i in jamCoin[::-1]])  # Note that we have to reverse for looks
            jamDivisors = ' '.join([str(i) for i in twoBitSums])
            results.append([jamString, jamDivisors])

        return results

    def process(self, cases):
        size, number = cases
        results = []
        middleCounter = 0
        jamCoinFound = 0

        baseArray = self.getBaseArrays(size)

        numFound = 0

        while jamCoinFound < number:
            jamCoin = [1] + self.getMidCoinBool(middleCounter, size - 2) + [1]
            divisors, isJamCoin = self.checkJamCoin(jamCoin, baseArray)

            if isJamCoin:
                jamCoinFound += 1
                jamString = ''.join([str(i) for i in jamCoin[::-1]])  # Note that we have to reverse for looks
                jamDivisors = ' '.join([str(i) for i in divisors])
                results.append([jamString, jamDivisors])
                # print numFound, jamString, jamDivisors
                numFound += 1

            middleCounter += 1
            if middleCounter % np.power(2, size - 2) == 0:
                break

        return results

    def checkJamCoin(self, jamCoin, baseArray):
        divisors = []
        canJam = []

        for base in baseArray:
            valueInBase = self.getNumInBase(base, jamCoin)
            isPrime, divisor = self.checkPrime(valueInBase)
            # print jamCoin[::-1], valueInBase, isPrime, divisor
            divisors.append(divisor)
            canJam.append(not isPrime)
            if (isPrime):
                break

        return divisors, np.all(canJam)

    def getNumInBase(self, baseArray, bitArray):
        return sum([a * b for a, b in zip(baseArray, bitArray)])

    def getBaseArrays(self, size):
        baseArray = []
        for i in range(2, 11):  # Base 2 to base 10
            bases = [0] * size
            for j in range(size):
                bases[j] = np.power(i, j)
            baseArray.append(bases)
        return baseArray

    def getMidCoinBool(self, counter, size):
        digits = counter
        boolArray = [0] * size
        index = 0
        while index < size:
            leftMostDigit = digits % 2
            boolArray[index] = leftMostDigit
            digits = int(np.floor(digits / 2))
            index += 1

        return boolArray  # [::-1]

    def checkPrime(self, num):
        divisor = 1

        if num < 2:
            return False, divisor

        if num == 2:
            return True, 2

        # Evens
        if not num & 1:
            return False, 2

        # Odds, range starts with 3 and only needs to go up the squareroot of num
        checkRange = range(3, int(num**0.5) + 1, 2)
        for x in checkRange:
            if num % x == 0:
                return False, x
            if x > 1000:
                #  print "Skipping.."
                return True, 0  # Skip, surely there are better ones

        return True, 0

def main():
    q3 = CoinJam()
    q3.run()


if  __name__ =='__main__':
    main()
