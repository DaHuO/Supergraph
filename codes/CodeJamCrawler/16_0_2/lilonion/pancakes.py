
#!/usr/bin/env python

import sys


def solveProblem(stack):
    switches = 0 
    last = ""
    for current in stack:
        if current != last:
            last = current
            switches += 1
    if not last:
        switches += 1
    return switches-1
    
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in xrange(n):
        stack = tuple(c == "+" for c in [x for x in sys.stdin.readline() if x in ('-', '+')])
        print "Case #%d: %s" % (i + 1, solveProblem(stack))
            
        
    
        