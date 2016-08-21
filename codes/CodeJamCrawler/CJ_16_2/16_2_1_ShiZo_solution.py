import sys

numberWords = [
    'ZERO',
    'TWO',
    'FOUR',
    'THREE',
    'ONE',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE'
]

wordNumbers = [
    0,
    2,
    4,
    3,
    1,
    5,
    6,
    7,
    8,
    9
]


def testWord(word, string):
    for char in word:
        if char not in string:
            return False

        if char == 'E':
            index = string.index(char)
            string = string[:index] + string[index + 1:]

        if char == 'N':
            index = string.index(char)
            string = string[:index] + string[index + 1:]

    return True


def removeWord(word, string):
    for char in word:
        index = string.index(char)
        string = string[:index] + string[index + 1:]

    return string


def getSolution(string, index, solution):
    if len(string) == 0:
        return solution

    if (index > 9):
        return False

    if testWord(numberWords[index], string):
        solution = solution + str(index)
        string = removeWord(numberWords[index], string)

        if len(string) > 0:
            return getSolution(string, int(index), solution)
        else:
            return solution
    else:
        return getSolution(string, int(index) + 1, solution)

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
    startString = inputf.readline()
    string = startString
    solution = ''

    for j in range(0, 10):
        while testWord(numberWords[j], string):
            solution = solution + str(wordNumbers[j])
            string = removeWord(numberWords[j], string)

    print(string)
    # print(getSolution(startString, 0, ''))

    outputf.write("Case #{}: {}\n".format(i, ''.join(sorted(solution))))
