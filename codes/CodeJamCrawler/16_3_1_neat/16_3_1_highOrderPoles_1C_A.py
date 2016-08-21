import numpy as np
from operator import itemgetter
from collections import Counter

class A:
    def readSenator(self):
        # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
        # This is all you need for most Google Code Jam problems.
        self.cases = []
        self.numCases = 0
        self.numCases = int(raw_input())  # read a line with a single integer
        for _ in xrange(1, self.numCases + 1):
            parties = int(raw_input())  # Parties
            polyNums = [int(s) for s in raw_input().split(" ")] # In parties
            partyName = [chr(ord('A') + i) for i in range(len(polyNums))]
            case = [parties, [list(a) for a in zip(partyName, polyNums)]]
            self.cases.append(case)

    def printOne(self, results):
        for i in xrange(len(results)):
            n = results[i]
            print "Case #{}: {}".format(i + 1, n)

    def run(self):
        self.readSenator()
        self.results = self.process(self.cases)
        self.printOne(self.results)

    def process(self, cases):
        results = []
        for n in cases:
            results.append(self.calculate(n))
        return results

    def calculate(self, case):
        result = []
        parties, senators = case
        senators = sorted(senators, key=lambda x: x[1])
        while (senators[-1][1] != 0):
            if (len(senators) > 2):
                if (senators[-1][1] == 1 and
                    senators[-1][1] == senators[-2][1] and
                    senators[-1][1] == senators[-3][1]):
                    senators[-1][1] = senators[-1][1] - 1
                    result.append(senators[-1][0])
                    senators = sorted(senators, key=lambda x: x[1])

            if senators[-1][1] == senators[-2][1]:
                senators[-1][1] = senators[-1][1] - 1
                senators[-2][1] = senators[-2][1] - 1
                result.append(senators[-1][0] + senators[-2][0])
            else:
                senators[-1][1] = senators[-1][1] - 2
                result.append(senators[-1][0] + senators[-1][0])

            senators = sorted(senators, key=lambda x: x[1])

        return " ".join(str(i) for i in result)


def main():
    q1 = A()
    q1.run()


if  __name__ =='__main__':
    main()