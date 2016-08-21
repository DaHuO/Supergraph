import itertools

def input(filename):
    lines = open(filename).read().split("\n")
    numCases = int(lines.pop(0))
    linesPerCase = int((len(lines)-1)/numCases)
    return [[lines.pop(0) for b in range(linesPerCase)] for a in range(numCases)]


def output(filename, strings):
    file = open(filename, 'w')
    for a in range(len(strings)):
        print("Case #"+str(a+1)+": "+strings[a]+"\n")
        file.write("Case #"+str(a+1)+": "+strings[a]+"\n")

cases = input("input.txt")

def validCircle(childs, circle):
    for idd in circle:
        bff = childs[idd-1]

        if bff not in circle:
            return False
        index = circle.index(idd)
        if len(circle)-1 == index:
            if (bff == circle[index-1] or bff == circle[0]) is False:
                return False
        elif index == 0:
            if (bff == circle[len(circle)-1] or bff == circle[index+1]) is False:
                return False
        else:
            if (bff == circle[index-1] or bff == circle[index+1]) is False:
                return False
    return True

def getList(beginID, list):
    currentChilds = [beginID]
    currentID = beginID
    while True:
        nextChild = list[currentID-1]
        if nextChild in currentChilds:
            return currentChilds
        currentID = nextChild
        currentChilds.append(nextChild)

mem = {}

def solve(n, ids):
    biggest = -1
    for a in range(len(ids)):
        curList = getList(a+1, ids)
        print(curList)
        if len(curList) == 6:
            print("66")
            print(curList)
        if validCircle(ids, curList):

            if biggest < len(curList):
                print("big")
                #print(curList)
                biggest = len(curList)

    return biggest

def solveUgly(n, ids):
    print(ids)
    for a in range(len(ids), -1, -1):
        for curList in itertools.permutations(range(1, len(ids)+1), a):
            if validCircle(ids, curList):
                return len(curList)

strings = []
for case in cases:
    print("case")
    strings.append(str(solveUgly(int(case[0]), [int(a) for a in case[1].split(" ")])))

print("solve"+str(solveUgly(4, [2, 3, 4, 1])))

output("output.txt", strings)
