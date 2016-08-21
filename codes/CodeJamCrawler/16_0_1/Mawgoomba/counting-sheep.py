# Google code jam 2016
# Qualification Round - A
# Markus Wind (MawGoomba)

input_file = open('A-large.in', 'r')
output_file = open('A-large.out', 'wb')

def countSheep(caseNumber, startingNumber):
    print "countSheep: {}, {}".format(caseNumber, startingNumber)

    remainingDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    I = 1
    N = startingNumber

    if startingNumber == 0:
        printResult(startingNumber, caseNumber, "INSOMNIA")

        return

    while len(remainingDigits) > 0:
        N = I * startingNumber
        I = I + 1

        currentNumber = str(N)

        for index, digit in enumerate(currentNumber):
            if int(digit) in remainingDigits:
                remainingDigits = deleteDigit(int(digit), remainingDigits)

    printResult(startingNumber, caseNumber, N)

def deleteDigit(seenDigit, remainingDigits):
    for index, digit in enumerate(remainingDigits):
        if digit == seenDigit:
            remainingDigits.pop(index)

            break

    return remainingDigits

def printResult(startingNumber, caseNumber, result):
    output_file.write("Case #{}: {}\n".format(caseNumber, result))

def readInputFile():
    numberOfCases = int(input_file.readline())

    for caseNumber in xrange(1, numberOfCases + 1):
        n = input_file.readline().strip('\n')

        countSheep(caseNumber, int(n))

# Running script here
readInputFile()
input_file.close()
output_file.close()
