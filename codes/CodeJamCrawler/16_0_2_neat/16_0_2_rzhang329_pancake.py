import sys

def numFlips(cakes):
    tempCakes = [x for x in cakes]
    index = len(cakes) - 1
    flips = 0
    while index >= 0:
        if not tempCakes[index]:
            tempCakes = [not x if i<=index else x for i,x in enumerate(tempCakes)]
            flips += 1
        index -= 1
    return flips

def boolConv(line):
    data = list(line)
    result = []
    for cake in data:
        if cake == '+':
            result.append(True)
        elif cake == '-':
            result.append(False)
    return tuple(result)

if __name__ == '__main__':
    inputFile = open(sys.argv[1], 'r')
    inputData = inputFile.read().splitlines()[1:]
    outputData = [numFlips(boolConv(x)) for x in inputData]
    outputFile = open("output.txt", 'w')
    for index,item in enumerate(outputData):
        outputFile.write("Case #{0}: {1}\n".format(index+1,item))
    inputFile.close()
    outputFile.close()
