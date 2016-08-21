from sets import Set

digits = set()

def main():
    f = open('A-large.in', 'r')
    out = open('outputfile.txt', 'w')
    numOfTestCases = int(f.readline())
    for case in range(1, (numOfTestCases+1)):
        N = int(f.readline())
        out.write('Case #' + str(case) + ': ' + str(startTestCase(N)) + '\n')
        digits.clear()


def startTestCase(k):
    if (k == 0):
        return 'INSOMNIA'
    x = 1
    output = countSheep(k, x)
    while (output == -1):
        output = countSheep(k, x)
        x += 1
    return output

def countSheep(n, i):
    value = n*i
    arrayOfDigits = str(value)
    for digit in arrayOfDigits:
        digits.add(digit)
        if (len(digits) == 10):
            return value
    return -1


if __name__ == "__main__": main()
