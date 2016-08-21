import sys

def findLast(num):
    current = 0
    check = 0
    digits = [False for x in range(10)]
    while (not all(digits)) and check < 1000:
        current += num
        pieces = findDigits(current)
        for i in pieces:
            if not digits[i]:
                digits[i] = True
                check = 0
        check += 1
    if check >= 1000:
        return "INSOMNIA"
    else:
        return current

def findDigits(num):
    numStr = list(str(num))
    return set(int(x) for x in numStr)

if __name__ == '__main__':
    fileName = sys.argv[1]
    inputFile = open(fileName, 'r')
    inputData = inputFile.read().splitlines()[1:]
    outputData = [findLast(int(x)) for x in inputData]
    outputFile = open("output.txt", 'w')
    for index,item in enumerate(outputData):
        outputFile.write("Case #{0}: {1}\n".format(index+1,item))
    inputFile.close()
    outputFile.close()
