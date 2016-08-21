import glob, time, string, re, math
from math import sqrt; from itertools import count, islice

#textFile = open("out_test.txt", "w")
textFile = open("output_large.txt", "w")
#textFile = open("output_small.txt", "w")
#open and read the input file
#sInputFileLoc = 'test.in'
sInputFileLoc = 'A-large.in'
#sInputFileLoc = 'A-small-attempt0.in'
sInputFile = open(sInputFileLoc)
sLineOutput = "Case #"
iLineRead = 0

def checkEqual2(iterator):
    return len(set(iterator)) <= 1

def counting_sheep(N):
    status2 = False
    NumVal2 = [0,0,0,0,0,0,0,0,0,0]
    if N == 0:
        val = 'INSOMNIA'
    else:
        for i in range(1000000):
            val = N*(i+1)
            valStr = str(val)
            for ch in valStr:
                NumVal2[int(ch)] = 1
                status2 = checkEqual2(NumVal2)
                if status2 == True:
                    break
            if status2 == True:
                break

        if status2 == False:
            val = 'INSOMNIA'
    return val
            

#Import the first line of the file. The first line contains how many different test cases are in the file being imported
iNumTestCases = int(sInputFile.readline())

#based on the numer of test cases in the first line, loop through these each one by one
for x in range(iNumTestCases):
    #import the first line of text
    sInputString = sInputFile.readline()
    resultsOut = counting_sheep(int(sInputString))
    
    textFile.write(sLineOutput+str(x+1)+ ": " + str(resultsOut) +"\n")

textFile.close()


