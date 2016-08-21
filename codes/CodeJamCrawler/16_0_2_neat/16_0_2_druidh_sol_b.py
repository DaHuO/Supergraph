#!/usr/bin/python2.7

for case in range(input()):
    s = raw_input()
    sol = 0
    for i in xrange(len(s)-1):
        if (s[i]!=s[i+1]):
            sol += 1
    if (s[-1] == '-'):
        sol += 1
   
    print 'Case #%s: %s' % ((case + 1), sol)

