import sys

inputfile = 'input.txt'
outputfile = 'output.txt'

try:
    inputfile = sys.argv[1]
except IndexError:
    inputfile = 'input.txt'
try:
    outputfile = sys.argv[2]
except IndexError:
    outputfile = 'output.txt'

inputf = open(inputfile, 'r')
outputf = open(outputfile, 'w')

t = int(inputf.readline())

for i in range(1, t + 1):
    pancakeStack = str(inputf.readline())
    flipCount = int(0)
    orderReady = False

    while not orderReady:
        if pancakeStack.find('-') == -1:
            orderReady = True
            break

        flipIndex = int(0)

        for p in range(len(pancakeStack)):
            currentSideUp = str(pancakeStack[:1])

            if pancakeStack[p:p+1] == currentSideUp:
                flipIndex = p
            else:
                break

        if not orderReady:
            flipCount += int(1)
            flipStack = pancakeStack[:flipIndex + 1]

            if flipStack[:1] == '-':
                flippedStack = '+' * len(flipStack)
            else:
                flippedStack = '-' * len(flipStack)

            pancakeStack = flippedStack + pancakeStack[flipIndex + 1:]

    outputf.write("Case #{}: {}\n".format(i, flipCount))
