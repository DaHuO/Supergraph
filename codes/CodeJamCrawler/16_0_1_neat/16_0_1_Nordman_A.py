import sys
from operator import add

inputFile = open(sys.argv[1], 'r')

#read params
numCases = int(inputFile.next())
#print "numCases : %d" % numCases

#read cases
N = [int(inputFile.next()) for x in range(numCases)]

digits = ['0','1','2','3','4','5','6','7','8','9']

for i in range(1, numCases+1):
    multiplier = 1
    digitsPresent = [0] * 10
    currentVal = N[i-1]

    if N[i-1] == 0:
        print "Case #%d: %s" % (i, "INSOMNIA")
    else:
        while digitsPresent.count(0) > 0:
            currentVal = multiplier*N[i-1]
            digitsPresent = map(add,digitsPresent, list(str(currentVal).count(x) for x in digits))
            #print digitsPresent
            multiplier += 1

        print "Case #%d: %d" % (i, currentVal)


inputFile.close()
