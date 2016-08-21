import time
outFile = "output.out"
inFile = "B-large.in"

def makeBoolStack(stringStack):
    boolStack = []
    for pancake in stringStack:
        if pancake == "+":
            boolStack.append(True)
        elif pancake == "-":
            boolStack.append(False)
    return boolStack

def flipStack(stack, numberToFlip):
    stackTop = stack[:numberToFlip]
    stackTop = stackTop[::-1]
    stackBottom = stack[numberToFlip:]
    for i in range(numberToFlip):
        stackTop[i] = not stackTop[i]
    stack = stackTop + stackBottom
    return stack

def allFaceUp(stack):
    return sum(stack) == len(stack)

def findTruesAtTop(stack):
    numTrues = 0
    stackLen = len(stack)
    for i in range(0,stackLen):
        if stack[i]:
            numTrues += 1
        else:
            return numTrues

def calculateFlips(stringStack):
    numFlips = 0
    stack = makeBoolStack(stringStack)
    stackLen = len(stack)
    while not allFaceUp(stack):
        topTs = findTruesAtTop(stack)
        if topTs > 0:
            stack = flipStack(stack, topTs)
            numFlips += 1
            continue
        for i in range(0,stackLen):
            if not stack[stackLen-i-1]:
                stack = flipStack(stack, stackLen-i)
                numFlips += 1
                break
    return numFlips

with open(inFile, "r") as f:
    with open(outFile, "w") as of:
        num = int(f.readline())
        content = [x.strip('\n') for x in f.readlines()]
        for i in range(num):
            numFlips = calculateFlips(content[i])
            of.write("Case #" + str(i+1) + ": " + str(numFlips) + "\n")
print("done!")
