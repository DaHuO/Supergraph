filename = 'A-large'

def countSheep(number):
    '''if all the digits are even it won't work ever, otherwise should work'''
    s = str(number)
    oddFound = False
    for x in s:
        if int(x) % 2 == 1:
            oddFound = True

    if int(s) == 0:
        return 'INSOMNIA'

    digits = []
    for i in range(0,10):
        digits.append(False)

    i = 0
    while False in digits:
        i = i + 1
        s = str(i*number)
        for x in s:
            digits[int(x)] = True

    return str(i*number)

inFile = open(filename + '.in','r')
outFile = open(filename + '.out','w')

numCases = int(inFile.readline())
print(numCases)

for i in range(1,numCases+1):
    outFile.write('Case #' + str(i) + ': ')
    outFile.write(countSheep(int(inFile.readline())))
    outFile.write('\n')

inFile.close()
outFile.close()
