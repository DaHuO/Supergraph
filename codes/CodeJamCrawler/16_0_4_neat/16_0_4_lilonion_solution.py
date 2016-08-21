
#!/usr/bin/env python

import sys

def getLocation(K, originals):
    #Originals should be of length C
    current = 1
    for i in originals:
        current = (current-1)*K + i
    return current

def solveProblem(K, C, S):
    if K/C > S:
        return "IMPOSSIBLE"
    else:
        current = 1
        locations = []
        while current <= K:
            current = min(current, K-C+1)
            originals = range(current, current+C+1)
            locations.append(getLocation(K, originals))
            current += C
    if C > S:
        locations = [getLocation(K, range(1, K+1))]
    locations = [str(e) for e in locations]
    return " ".join(locations)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in xrange(n):
        K, C, S = (int(c) for c in sys.stdin.readline().split(" "))
        print "Case #%d: %s" % (i + 1, solveProblem(K, C, S))
            
        
    
        