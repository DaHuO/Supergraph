def dataParser(fileDir):
    inputfile = open(fileDir,'rU')
    nbrOfCases = int(inputfile.readline())
    cases = [0 for i in range(nbrOfCases)]
    for i in range(nbrOfCases):
        cases[i] = int(inputfile.readline())
    inputfile.close()
    return cases
def removeDigits(nbr,digits):
    if nbr==0 and 0 in digits:
        digits.remove(0)
    while nbr>0:
        if nbr%10 in digits:
            digits.remove(nbr%10)
        nbr/=10


cases = dataParser('test.txt')
outputFile = open('out.txt','w')
for i in xrange(len(cases)):
    digits = set([0,1,2,3,4,5,6,7,8,9])
    N = cases[i]
    currentNbr = N
    if currentNbr==0:
        outputFile.write('Case #' + str(i+1) + ': INSOMNIA\n')
    else:
        while True:
            removeDigits(currentNbr,digits)
            if len(digits)==0:
                outputFile.write('Case #'+str(i+1)+': '+str(currentNbr)+'\n')
                break
            currentNbr += N
