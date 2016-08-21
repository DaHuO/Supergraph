import utils

if __name__ == "__main__":
    inputFile = "D-small-attempt0.in"
    #inputFile = "C-small-attempt0.in"
    #inputFile = "A-large.in.txt"
    #inputFile = "inputQ3"
    outputFile = "outputQ4"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.strip()
    print cases
    for index in range(1, int(cases) + 1):
        print "case ", index
        outputString = "Case #" + str(index) + ": "
        
        rowData = inputData.next()
        rowData = rowData.strip()
        print rowData
        strs = rowData.split(' ')
        K = int(strs[0])
        C = int(strs[1])
        S = int(strs[2])
        res = list(range(1,S + 1))
        reslist = ' '.join(str(x) for x in res)
        outputString += reslist
        outputString += "\n"
        print outputString
        outputData.write(outputString)



            
