import os
import getopt
import sys
import time

def simulate(inputfile):
    f = open(inputfile, 'r')
    counter = 0
    with open("case1.out","a") as outfile: 
        for line in f:
            if (counter == 0):
                counter+=1
                continue
            val = line.strip()
            output = sheepCounter(val)
            outfile.write('Case #' + str(counter) + ': ' + str(output) + '\n')
            counter+=1

def sheepCounter(val):
    if (int(val) == 0):
        return 'INSOMNIA'
    iterationVal = val
    counter = 1
    memo = [0,0,0,0,0,0,0,0,0,0]
    while (0 in memo):
        iterationVal = str(int(val)*counter)
        counter += 1
        for char in list(iterationVal):
            currentNum = int(char)
            memo[currentNum] = 1
    return iterationVal

# python ps1.py -i inputfile

def usage():
    print "usage: " + sys.argv[0] + " -i inputfile"

inputfile = None

try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:')
except getopt.GetoptError, err:
    usage()
    sys.exit(2)
for o, a in opts:
    if o == '-i':
        inputfile = a
    else:
        assert False, "unhandled option"
if inputfile == None:
    usage()
    sys.exit(2)
    
simulate(inputfile)
