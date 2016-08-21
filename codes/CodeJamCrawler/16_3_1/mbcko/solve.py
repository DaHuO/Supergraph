#!/usr/bin/env python

import sys
import time

def mapSenator(n):
    return chr(65 + n)
    
def solve(*args):
    (N,) = args
    P = [int(one.strip()) for one in sys.stdin.readline().split()]
    retval = []
    while any(P):
        Ps = sorted(P)
        #print P, 
        if Ps[-2] == 1 and Ps[-1] == 2:
            max1 = P.index(Ps[-1])
            max2 = P.index(Ps[-2])
            
            retval.append(mapSenator(max1))
            P[max1] -= 1
            #print "#1",
        elif Ps[-2] == 1 and Ps[-1] == 1:
            max1 = P.index(Ps[-1])
            max2 = P.index(Ps[-2])
            if max1 == max2:
                max2 = P.index(Ps[-2], max2 + 1)
            
            if sum(P) % 2 == 0:
                retval.append(mapSenator(max1) + mapSenator(max2))
                P[max1] -= 1
                P[max2] -= 1
            else:
                retval.append(mapSenator(max1))
                P[max1] -= 1
            #print "#2",
        elif Ps[-2] > 0:
            max1 = P.index(Ps[-1])
            max2 = P.index(Ps[-2])
            if max1 == max2:
                max2 = P.index(Ps[-2], max2 + 1)
        
            retval.append(mapSenator(max1) + mapSenator(max2))
            P[max1] -= 1
            P[max2] -= 1
            #print "#3",
        elif Ps[-1] > 0:
            max1 = P.index(Ps[-1])
            sens = mapSenator(max1)
            P[max1] -= 1
            if P[max1] > 0:
                sens += mapSenator(max1)
                P[max1] -= 1
            retval.append(sens)
            #print "#4",
        else:
            #print "wtf"
            break
        #print retval[-1]
            
    return " ".join(retval)

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        params = [int(one.strip()) for one in sys.stdin.readline().split()]
        result = solve(*params)
        print "Case #%d: %s" % (caseNumber, result)
       
if __name__ == '__main__':
    main()


