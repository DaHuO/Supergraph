import numpy
import math

class caseC:

    def __init__(self, case, n, j):
        self.caseNum = case
        self.n = n
        self.j = j

class Coin :

    def __init__(self, coin):
        self.coinString = coin
        self.divisors = []

    def isCoin(self):
        for i in range(2,11) :
            divisor = getDivisor(self.fromBase(i))
            if not divisor :
                return False
            else :
                self.divisors.append(divisor)
            # if is_prime(self.fromBase(i)) :
            #     return False
        return True
        pass

    def fromBase(self, base):
        return int(self.coinString, base)
        pass


def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

# credit: http://stackoverflow.com/questions/17298130/working-with-large-primes-in-python
def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(math.sqrt(num)) + 1, 2))

def getDivisor(num) :
    for i in mrange(3, min(int(math.sqrt(num)) + 1, 10000), 2):
        if(num % i == 0) :
            return i

    return False

def getCases(filename):
    cases = []
    f = open(filename, 'r')
    line = f.readline()
    caseCount = int(line)
    line = f.readline()
    caseNum = 1
    while line:
        line = line.rstrip('\n')
        vals = str(line).split(' ')
        case = caseC(caseNum, int(vals[0]), int(vals[1]))

        caseNum += 1
        line = f.readline()
        cases.append(case)

    if(len(cases) != caseCount) :
        print("Wrong cases count!")

    return cases

def main():
    file = "C-large"
    cases = getCases(file + '.in')
    case = cases[0]
    testString = "1" + ("0" * (case.n-2)) + '1'
    coins = []

    while(len(coins) < case.j) :
        coin = Coin(testString)
        if(coin.isCoin()) :
            coins.append(coin)
        testString = numpy.base_repr(int(testString, 2) + 2, 2)

    outFile = open(file + '.output.txt', "w")
    outFile.write('Case #1:\n')
    for coin in coins :
        # ansLine = "Case #" + str(case.caseNum) + ": " + answer + "\n"
        ansLine = coin.coinString + ' ' + (' '.join(str(x) for x in coin.divisors)) + "\n"
        outFile.write(ansLine)
    pass

def test() :
    coin = Coin("100011")
    print(coin.isCoin())
    print(coin.divisors)
    # test = is_prime(100011)
    pass

if __name__ == "__main__":
    main()