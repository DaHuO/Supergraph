import utils


def checkOnes(l):
    ones = 0
    last = -1
    for i in range(len(l)):
        if i > 0:
            last = l[i - 1]
        if l[i] == 0:
            if last == 1:
                ones += 1
            else:
                continue
        else:
            if last == 1:
                continue
            else:
                continue
    return ones

if __name__ == "__main__":
    inputFile = "inputQ2"
    inputFile = "B-small-attempt0.in"
    #inputFile = "test"
    inputFile = "B-large.in"
    #inputFile = "A-large.in.txt"
    #inputFile = "inputQ3"
    outputFile = "outputQ2"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.strip()
    print cases
    for index in range(1, int(cases) + 1):
        print "case ", index
        rowData = inputData.next()
        rowData = rowData.strip()
        length = len(rowData)
        l = [0] * length
        for i in range(length):
            if rowData[i] == "+":
                l[i] = 1

        ones = checkOnes(l)
        print ones
        o = ones * 2
        if l[0] == 0:
            o += 1


        outputString = "Case #" + str(index)+ ": " + str(o) + "\n"
        print outputString
        outputData.write(outputString)
                
            
