'''
Created on Apr 9, 2016

@author: roadkill
'''

def solve(plates):
    switches = 0
    first_flip_found = False
    for c in reversed(plates):
        if not first_flip_found:
            if c == '+':
                continue
            else:
                first_flip_found = True
                current = c
                switches += 1
        else: 
            if c != current:
                switches += 1
                current = c
    return switches

for case in xrange(input()):
    plates = raw_input()
    
    res = solve(plates)

    print "Case #%i: %d" % (case+1, res)