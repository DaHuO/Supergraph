import numpy as np

class Pancakes:
    def readCakes(self):
        # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
        # This is all you need for most Google Code Jam problems.
        self.cases = []
        self.numCases = 0

        self.numCases = int(raw_input())  # read a line with a single integer
        for i in xrange(1, self.numCases + 1):
            n = raw_input()  # read a list of integers, 2 in this case
            stack = []
            for side in n:
                if side == '+':
                    stack.append(True)
                else:
                    stack.append(False)
            self.cases.append(stack)

    def printOne(self, results):
        for i in xrange(len(results)):
            n = results[i]
            print "Case #{}: {}".format(i + 1, n)

    def run(self):
        self.readCakes()
        self.results = self.process(self.cases)
        self.printOne(self.results)

    def process(self, cases):
        results = []
        for n in cases:
            results.append(self.happySideUp(n))

        return results

    def happySideUp(self, n):
        step = 0
        stack = n

        while not np.all(stack):
            firstPancake = stack[0]
            flipIndex = 0

            if (len(stack) > 1):
                while stack[flipIndex + 1] == firstPancake:
                    flipIndex += 1
                    if (flipIndex + 1) == len(stack):
                        break

            # Now flip greedily
            stack = self.flipStack(stack, flipIndex)
            step += 1

        return step

    def flipStack(self, stack, index):
        newStack = [not i for i in stack[index::-1]] + stack[index+1:]
        return newStack


def main():
    q2 = Pancakes()
    q2.run()


if  __name__ =='__main__':
    main()