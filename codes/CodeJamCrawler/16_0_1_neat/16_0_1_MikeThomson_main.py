__author__ = 'Mike'

import pprint
import sys
import math
#import resource
#sys.setrecursionlimit(10000)
#resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

pp = pprint.PrettyPrinter(indent=2)

class caseA :

    def __init__(self, case, num):
        self.caseNum = case
        self.counter = 1
        self.initialNum = num
        self.num = num
        self.seenNums = set([])
        self.allNums = set([
            1,2,3,4,5,6,7,8,9,0
        ])
        self.updateSeen()

    def nextNum(self):
        self.counter += 1
        self.num = self.counter * self.initialNum
        self.updateSeen()
        pass

    def canSleep(self):
        # if(self.seenNums == self.allNums) :
        if(len(self.seenNums) == 10) :
            return True
        return False
        pass

    def isInsomniac(self):
        return self.num == 0
        pass

    def updateSeen(self):
        for digit in str(self.num) :
            self.seenNums.add(int(digit))

        pass


def getCases(filename):
    cases = []
    f = open(filename, 'r')
    line = f.readline()
    caseCount = int(line)
    line = f.readline()
    caseNum = 1
    while line:
        line = line.rstrip('\n')
        case = caseA(caseNum, int(line))

        caseNum += 1
        line = f.readline()
        cases.append(case)

    if(len(cases) != caseCount) :
        print("Wrong cases count!")

    return cases


def main():
    file = "A-large"
    cases = getCases(file + '.in')
    for case in cases  :
        while not case.canSleep() and not case.isInsomniac() :
            case.nextNum()

    outFile = open(file + '.output.txt', "w")
    for case in cases :
        answer = 'INSOMNIA'
        if not case.isInsomniac() :
            answer = str(case.num)
        ansLine = "Case #" + str(case.caseNum) + ": " + answer + "\n"
        outFile.write(ansLine)
    pass

if __name__ == "__main__":
    main()