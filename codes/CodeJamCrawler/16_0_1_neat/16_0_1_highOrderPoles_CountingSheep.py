import numpy as np

class CountingSheep:
    def readOne(self):
        # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
        # This is all you need for most Google Code Jam problems.
        self.cases = []
        self.numCases = 0

        self.numCases = int(raw_input())  # read a line with a single integer
        for i in xrange(1, self.numCases + 1):
            n = int(raw_input())  # read a list of integers, 2 in this case
            self.cases.append(n)

    def printOne(self, results):
        for i in xrange(len(results)):
            n = results[i]
            print "Case #{}: {}".format(i + 1, n)

    def run(self):
        self.readOne()
        self.results = self.process(self.cases)
        self.printOne(self.results)

    def process(self, cases):
        results = []
        for n in cases:
            results.append(self.countSheep(n))

        return results

    def countSheep(self, n):
        result = "INSOMNIA"
        status = [False] * 10
        counter = 1

        while not np.all(status):
            sheep = counter * n
            if sheep == 0:
                break;
            else:
                result = sheep

            newStatus = self.getDigits(sheep)
            status = np.logical_or(status, newStatus)
            counter += 1

        return result

    def getDigits(self, sheep):
        digits = sheep
        status = [False] * 10

        while digits != 0:
            leftMostDigit = digits % 10
            status[leftMostDigit] = True
            digits = int(np.floor(digits / 10))

        return status


def main():
    q1 = CountingSheep()
    q1.run()


if  __name__ =='__main__':
    main()