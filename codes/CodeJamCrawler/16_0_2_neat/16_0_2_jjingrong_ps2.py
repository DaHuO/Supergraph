import os
import getopt
import sys
import time

def simulate(inputfile, outputfile):
    f = open(inputfile, 'r')
    counter = 0
    with open(outputfile,"a") as outfile: 
        for line in f:
            if (counter == 0):
                counter+=1
                continue
            val = line.strip()
            output = pancakeFlipper(val)
            outfile.write('Case #' + str(counter) + ': ' + str(output) + '\n')
            counter+=1

def pancakeFlipper(val):
    pancakeArr = list(val)
    counter = 0
    while ('-' in pancakeArr):
        # logic for determining index
        # find idx of last '-' in arr
        # flip consecutively '-' pancakes from that to start
        
        # last idx of '-'
        lastIdx = ''.join(pancakeArr).rfind('-')
        if (lastIdx == -1): # not found
            return counter
        pancakeArr = flipPancakes(pancakeArr, lastIdx)
        counter += 1
    return counter 


# Flips number of pancakes 
def flipPancakes(arr, idx):
    topStack = arr[:idx+1]
    bottomStack = arr[idx+1:]
    
    # flip the topstack
    invertedTop = []
    for pancake in topStack:
        if (pancake == '-'):
            invertedTop.append('+')
        if (pancake == '+'):
            invertedTop.append('-')
    return invertedTop + bottomStack

# python ps2.py -i inputfile

def usage():
    print "usage: " + sys.argv[0] + " -i inputfile -o outputfile"

inputfile = None
outputfile = None

try:
    opts, args = getopt.getopt(sys.argv[1:], 'i: o:')
except getopt.GetoptError, err:
    usage()
    sys.exit(2)
for o, a in opts:
    if o == '-i':
        inputfile = a
    elif o == '-o':
        outputfile = a
    else:
        assert False, "unhandled option"
if inputfile == None or outputfile == None:
    usage()
    sys.exit(2)
    
simulate(inputfile, outputfile)
