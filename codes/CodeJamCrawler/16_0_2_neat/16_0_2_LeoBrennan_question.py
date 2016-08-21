import sys

name = "B-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

global flipCount
global line

def start():
    global line
    global flipCount
    
    for testCase in range(1, testCases + 1):
        line = str(input())
        flipCount = 0
        firstCharacter = line[0]
    
        if (len(line) == 1):
            if (line[0] == "-"):
                flipCount = 1
        else:
            finished = checkIfAllSame()
            while not finished:
                finished = checkIfAllSame()
        print("Case #" + str(testCase) + ": " + ("%i" % flipCount))

def checkIfAllSame():
    global line
    for nextIndex in range(1, len(line)):
        if (line[nextIndex] != line[0]):
            line = flipSection(nextIndex - 1)
            return False
    if (line[0] == "-"):
        line = flipSection(len(line) - 1)
        return True
    else:
        return True


def flipSection(i):
    global flipCount
    
    newList = list(line)
    for index in range(0, i + 1):
        if (newList[index] == "+"):
            newList[index] = "-"
        else:
            newList[index] = "+"
    flipCount = flipCount + 1
    newLine = ''.join(newList)
    return newLine

start()