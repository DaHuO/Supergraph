'''
Created on Apr 9, 2016

@author: roadkill
'''

def solve(n):
    if n == 0:
        return 0
    seen = set()
    i = 1
    current = n
    while(True):
        for c in "%d" % current:
            seen.add(c)
        if len(seen) >= 10:
            return current
        i = i + 1
        current = i * n

for case in xrange(input()):
    N = int(raw_input())
    
    res = solve(N)
    
    if res == 0:
        print "Case #%i: INSOMNIA" % (case+1)
    else:
        print "Case #%i: %d" % (case+1, res)