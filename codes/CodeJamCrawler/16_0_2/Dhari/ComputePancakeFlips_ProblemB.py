import sys
import os

def ComputeMinFlipcount(s):
    flipCount = 0
    lastSeen = "+"
    for c in s[-1::-1]:
        if c != lastSeen:
            flipCount += 1
            lastSeen = c
    return flipCount

def main():

    T = int(raw_input())

    for testNo in xrange(1,T+1):
        s = raw_input()
        print "Case #%d: %d"%(testNo,ComputeMinFlipcount(s))

if __name__ == "__main__":
    main()
    
