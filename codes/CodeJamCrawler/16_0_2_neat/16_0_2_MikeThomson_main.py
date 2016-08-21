

class caseB :

    def __init__(self, case, stack):
        self.caseNum = case
        self.stack = stack
        self.flipCount = 0

    def flip(self, index):
        # pick up the stack
        smallStack = self.stack[:index]
        baseStack = self.stack[index:]
        # reverse the stack order
        smallStack = smallStack[::-1]
        # reverse the pancake sides
        topStack = ''
        for pancake in smallStack :
            newCake = '+' if (pancake == '-') else '-'
            topStack += newCake

        self.stack = topStack + baseStack
        self.flipCount += 1
        pass

    def isHappy(self):
        for pancake in self.stack :
            if(pancake == '-') :
                return False

        return True
        pass

    def getFlipIndex(self):
        if(self.stack[0] == '+') :
            # go until we find a -
            index = 0
            for pancake in self.stack :
                if(pancake == '+') :
                    index += 1
                else :
                    return index


        index = len(self.stack)
        for digit in self.stack[::-1] :
            if(digit == '-') :
                return index
            index -= 1
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
        case = caseB(caseNum, str(line))

        caseNum += 1
        line = f.readline()
        cases.append(case)

    if(len(cases) != caseCount) :
        print("Wrong cases count!")

    return cases

def main():
    file = "B-large"
    cases = getCases(file + '.in')
    for case in cases  :
        while not case.isHappy() :
            case.flip(case.getFlipIndex())

    outFile = open(file + '.output.txt', "w")
    for case in cases :
        answer = str(case.flipCount)
        ansLine = "Case #" + str(case.caseNum) + ": " + answer + "\n"
        outFile.write(ansLine)
    pass

if __name__ == "__main__":
    main()