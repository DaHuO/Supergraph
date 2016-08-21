def dataParser(fileDir):
    inputfile = open(fileDir,'rU')
    nbrOfCases = int(inputfile.readline())
    cases = [None for i in range(nbrOfCases)]
    for i in range(nbrOfCases):
        cases[i] = inputfile.readline()
    inputfile.close()
    return cases

cases = dataParser('test.txt')
outputFile = open('out.txt','w')
for i in range(len(cases)):
    x = cases[i]
    nbrOfDigits = [0]*10
    nbrOfDigits[0] = x.count('Z')
    nbrOfDigits[2] = x.count('W')
    nbrOfDigits[4] = x.count('U')
    nbrOfDigits[6] = x.count('X')
    nbrOfDigits[8] = x.count('G')
    nbrOfDigits[7] = x.count('S') - nbrOfDigits[6]
    nbrOfDigits[5] = x.count('V') - nbrOfDigits[7]
    nbrOfDigits[3] = x.count('R') - nbrOfDigits[0] - nbrOfDigits[4]
    nbrOfDigits[9] = x.count('I') - nbrOfDigits[6] - nbrOfDigits[8] - nbrOfDigits[5]
    nbrOfDigits[1] = x.count('N') - nbrOfDigits[7] - 2*nbrOfDigits[9]
    output = [0]*sum(nbrOfDigits)
    idx = 0
    for j in range(10):
        while(nbrOfDigits[j]>0):
            output[idx] = j
            idx+=1
            nbrOfDigits[j]-=1
    outputFile.write('Case #' + str(i + 1) + ': ')
    for k in range(len(output)):
        outputFile.write(str(output[k]))
    outputFile.write('\n')
outputFile.close()
