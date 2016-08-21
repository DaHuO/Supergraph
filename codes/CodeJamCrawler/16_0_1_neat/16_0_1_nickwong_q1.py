#!/usr/bin/python
# Usage:
#sh-4.3$ python q1.py 5 0 1 2 11 1692
#case #1: INSOMNIA
#case #2: 10
#case #3: 90
#case #4: 110
#case #5: 5076
import sys
allOnes = list("1111111111")

def checkBits(s, bits):
    for c in str(s):
        bits[ord(c)-48] = '1'
    return cmp(bits, allOnes)

for i, arg in enumerate(sys.argv[2:]):
    inNum = int(arg)
    if inNum == 0:
        print 'case #%d: INSOMNIA'%(i+1)
        continue
    numBits = [0] * 10
    while checkBits(inNum, numBits) != 0:
        inNum += int(arg)
    print 'case #%d: %s'%(i+1, inNum)
