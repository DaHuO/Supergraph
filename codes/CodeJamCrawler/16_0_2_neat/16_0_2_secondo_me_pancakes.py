import sys

lines = open(sys.argv[1]).readlines()

T = int(lines[0])

casenum = 0

for line in lines[1:]:
    casenum += 1
    s = line.strip() + '+'

    transitions = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            transitions += 1

    print 'case #' + str(casenum) + ": " + str(transitions)
        
