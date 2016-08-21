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
    inputString = inputf.readline()
    resultString = inputString[:1]

    for k in range(1, len(inputString)):
        if inputString[k] < resultString[0]:
            resultString += inputString[k]
        else:
            resultString = inputString[k] + resultString

    outputf.write("Case #{}: {}\n".format(i, resultString))
