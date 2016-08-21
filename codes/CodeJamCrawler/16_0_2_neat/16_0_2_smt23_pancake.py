filename = 'B-large'

def pancake(stack):
    '''if the last pancake is -, needs a flip, otherwise a flip for every change in sign'''

    stack = stack[0:-1]

    flips = 0

    if stack[-1] == '-':
        flips = 1

    first = stack[0]

    for x in stack:
        if x != first:
            flips = flips + 1
            first = x

    return str(flips)

inFile = open(filename + '.in','r')
outFile = open(filename + '.out','w')

numCases = int(inFile.readline())
print(numCases)

for i in range(1,numCases+1):
    outFile.write('Case #' + str(i) + ': ')
    outFile.write(pancake(inFile.readline()))
    outFile.write('\n')

inFile.close()
outFile.close()
