#!/usr/bin/env python

#Take N in parameter
#and count untill the 10
#digits be seen
def lastNumber(N):
    digits = dict()
    lastNum = int(N)


    #If impossible
    if (2 * int(N) == int(N)):
        return "INSOMNIA"
    else:
        #While Bleatrix hasn't seen 10 digits
        while (len(digits) < 10):
            #Look over every digit
            for char in str(lastNum):
                digits[char] = True
            #Increment only if necessary
            if (len(digits) < 10):
                lastNum += int(N)
    return str(lastNum)



def main():
    result = ""
    i = 1
    #Open the input file
    with open("A-large.in", 'r') as inputFile:
        testCasesNumber = inputFile.readline()
        #Read every case
        for N in inputFile:
            result += "Case #" + str(i) + ": "  + lastNumber(N) + '\n'
            i += 1
    #Write result
    with open("output.txt", 'w') as outputFile:
        outputFile.write(result)
main()
