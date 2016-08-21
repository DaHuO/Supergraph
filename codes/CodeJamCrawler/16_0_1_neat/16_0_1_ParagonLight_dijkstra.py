import utils


def checkDigits(n, l):
    strn = str(n)
    for i in range(len(strn)):
        l[int(strn[i])] = 1
    return l

def isAsleep(l):
    for i in range(len(l)):
        if l[i] == 0:
            return False
    return True


if __name__ == "__main__":
    inputFile = "inputQ1"
    #inputFile = "test"
    inputFile = "A-small-attempt0.in"
    inputFile = "A-large.in"
    #inputFile = "A-large.in.txt"
    #inputFile = "inputQ3"
    outputFile = "outputQ1"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.strip()
    print cases
    for index in range(1, int(cases) + 1):
        print "case ", index
        rowData = inputData.next()
        rowData = rowData.strip()
        N = int(rowData)
        print N
        i = 1
        l = [0] * 10
        base = [0] * 10
        base = checkDigits(N, base)
        while not isAsleep(l):
            n = N * i
            l = checkDigits(n, l)
            if i == 10000:
                break
            i += 1

        o = "INSOMNIA"
        if isAsleep(l):
            o = str((i - 1) * N)


        outputString = "Case #" + str(index)+ ": " + o + "\n"
        print outputString
        outputData.write(outputString)
                
            
