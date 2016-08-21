import sys

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
    digitsSeen = []

    def __init__(self, caseNumber, caseInfo):
        self.number = caseNumber
        self.params = caseInfo

    def checkDigits(self, n):
        n_str = str(n)
        for i in range(0, len(n_str)):
            self.digitsSeen[int(n_str[i])] = True

    def seenAllDigits(self):
        result = True
        i = 0
        while result and i < len(self.digitsSeen):
            result = result and self.digitsSeen[i]
            i = i + 1
        return result

    def solve(self):
        self.digitsSeen = [False, False, False, False, False, False, False, False, False, False]
        n = int(self.params[0])
        currentNumber = n

        if n == 0:
            result = "INSOMNIA"
        else:
            i = 2;
            self.checkDigits(currentNumber)
            while not self.seenAllDigits():
                    currentNumber = i * n
                    self.checkDigits(currentNumber)
                    i = i + 1

            result = str(currentNumber)
        return "Case #" + str(self.number) + ": " + result


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
