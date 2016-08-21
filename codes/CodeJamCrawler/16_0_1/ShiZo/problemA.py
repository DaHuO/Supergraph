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
    n = int(1)
    rangeLimit = 200
    base = inputf.readline()
    currentNumbersSeen = ''
    lastNumber = base

    while (n < 200):
        tmpValue = int(n) * int(base)

        j = 0

        for j in range(len(str(tmpValue))):
            number = str(tmpValue)[j:j+1]

            if number not in currentNumbersSeen:
                currentNumbersSeen += str(number)

        print(n)
        print(tmpValue)
        print(currentNumbersSeen)

        if len(currentNumbersSeen) >= 10:
            lastNumber = tmpValue
            break

        n += int(1)

    if n == 200:
        outputf.write("Case #{}: INSOMNIA\n".format(i))
    else:
        outputf.write("Case #{}: {}\n".format(i, lastNumber))
