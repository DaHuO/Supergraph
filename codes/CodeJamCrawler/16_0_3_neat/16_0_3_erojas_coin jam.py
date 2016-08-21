import sys
from math import sqrt;
from itertools import count, islice

class InputFile:
    cases = 0
    filename = ''
    caseLength = 0
    lines = []

    def __init__(self, filename, caseLength):
        self.filename = filename
        self.caseLength = caseLength

    def read(self):
        with open(self.filename, 'r') as f:
            self.lines = f.readlines()
        self.lines = [line.strip() for line in self.lines]
        self.cases = int(self.lines[0])

    def getCases(self):
        return self.cases

    def getCase(self, index):
        caseLines = []
        startOffset = (index-1)*self.caseLength + 1
        endOffset = index*self.caseLength + 1
        for i in range(startOffset, endOffset):
            caseLines.append(self.lines[i])
        return caseLines


class CaseSolver:
    def __init__(self, caseNumber, caseInfo):
        self.number = caseNumber
        self.params = caseInfo
        self.numbersFound = []

    def divisorGenerator(self, token, base):
        n = int(token, base)
        for i in xrange(2, int(sqrt(n)) + 1):
            if n%i == 0:
                return str(n/i)

    def isPrime(self, token, base):
        n = int(token, base)
        return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

    def getNextNumber(self, token):
        n = int(token, 2)
        n = n + 2;
        return list("{0:b}".format(n))

    def solve(self):
        (N, J) = self.params[0].split()
        N = int(N)
        J = int(J)

        start = [1]
        for i in range (0, N - 2):
            start.append(0)
        start.append(1)
        bases = range(2, 11)
        result = ""

        while len(self.numbersFound) < J:
            number = "".join(str(i) for i in start)
            isNotPrime = True
            for b in bases:
                isNotPrime = isNotPrime and (not self.isPrime(number, b))

            if isNotPrime:
                divisors = []
                for b in bases:
                    divisors.append(self.divisorGenerator(number, b))
                result = result + number + " " + " ".join(divisors) + "\r\n"
                self.numbersFound.append(number)

            start = self.getNextNumber(number)

        return "Case #" + str(self.number) + ":\n" + result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # 1. Update the number of lines per case
        linesPerCase = 1
        input_file = InputFile(sys.argv[1], linesPerCase);
        input_file.read()
        for i in range(1, input_file.getCases() + 1):
            print CaseSolver(i, input_file.getCase(i)).solve()
    else:
        usage = "Usage :"
        usage = usage + sys.argv[0]
        usage = usage + " <input_file>"
        print usage
