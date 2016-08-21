import glob, time, string, re, math
from math import sqrt; from itertools import count, islice

textFile = open("out_test.txt", "w")
#textFile = open("output_large.txt", "w")
#textFile = open("output_small.txt", "w")
#open and read the input file
#sInputFileLoc = 'test.in'
#sInputFileLoc = 'C-large-1.in'
sInputFileLoc = 'C-small-attempt1.in'
sInputFile = open(sInputFileLoc)
sLineOutput = "Case #"
iLineRead = 0

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def all_jamcoin(jcLength):
    jcLength = jcLength - 2
    for i in xrange(2**jcLength):
        s = bin(i)[2:]
        s = "0" * (jcLength-len(s)) + s
        yield '1' + s + '1'
        
def divGen(c):
    divs = []
    for w in xrange(1, int(math.sqrt(c) + 1)):
        if c % w == 0:
            yield w
            if w*w != c:
                divs.append(c / w)
                if ((c / w) != 1) and ((c / w) != c):
                    break
    for divisor in reversed(divs):
        yield divisor

def create_jamcoin(jcLength, jcNumber):
    if jcLength >= 3:
        possibleJamcoin = list(all_jamcoin(jcLength))
        finalJamCoin = []
        for x in possibleJamcoin:
            checkVal = []
            isPrime = False
            for y in xrange(9):
                val = int(x,y+2)
                if is_prime(int(val)) == True:
                    isPrime = True
                    break
                
                possibleList = list(divGen(val))
                checkVal.append(possibleList[1])
            if isPrime == False:
                checkVal.insert(0,x)
                finalJamCoin.append(checkVal)
            if len(finalJamCoin) > jcNumber:
                break
        #remove all but the requested number
        return finalJamCoin[:jcNumber]


#Import the first line of the file. The first line contains how many different test cases are in the file being imported
iNumTestCases = int(sInputFile.readline())

#based on the numer of test cases in the first line, loop through these each one by one
for x in range(iNumTestCases):
    #import the first line of text
    sInputString = sInputFile.readline()
    sInputString = sInputString.split()
    #separate out the items into an array
    jcLength = int(sInputString[0])
    jcNumber = int(sInputString[1])

    #print(sInputString)
    #print jcLength
    #print jcNumber
    resultsOut = create_jamcoin(jcLength, jcNumber)    
    
    textFile.write(sLineOutput+str(x+1)+ ":\n")
    for x in range(len(resultsOut)):
        textFile.write(str(resultsOut[x][0]) + " " + str(resultsOut[x][1]) + " " + str(resultsOut[x][2]) + " " + str(resultsOut[x][3]) + " " + str(resultsOut[x][4]) + " "
                       + str(resultsOut[x][5]) + " " + str(resultsOut[x][6]) + " " + str(resultsOut[x][7]) + " " + str(resultsOut[x][8]) + " " + str(resultsOut[x][9]) + " " + "\n")

textFile.close()


