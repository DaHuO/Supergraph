import sys
import itertools

def formatOutput(n, result):
    return 'Case #' +  str(n) + ': ' + result + '\n'

file = open(sys.argv[1])
output = open('output.txt', 'w')
nTests = int(file.readline())

HAPPY = '+'
SAD = '-'

testNb = 1
for line in itertools.islice(file, 0, nTests+1):     
    stack = line.replace('\n', '')
    nFlips = 0
    
    while SAD in stack:
        sPos = stack.index(SAD)
        if sPos != 0:
            stack = (sPos)*SAD + stack[sPos+1:]
            nFlips += 1
        if HAPPY in stack:
            hPos = stack.index(HAPPY)
            stack = (hPos)*HAPPY + stack[hPos+1:]
            nFlips += 1
        else:
            stack = stack.replace(SAD, HAPPY)
            nFlips += 1

    output.write(formatOutput(testNb, str(nFlips)))
    testNb += 1

   