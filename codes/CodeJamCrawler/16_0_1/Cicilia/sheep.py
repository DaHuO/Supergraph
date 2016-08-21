#!/usr/bin/env python

import sys

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    if n == 0:
        print "Case #%d: INSOMNIA" %(i)
        continue
    no_see = "0123456789"
    for j in range(1, 10**5-1):
        now = str(n*j)
        #print "#%d-%d now %s no_see %s" % (i, j, now, no_see)
        for x in range(len(no_see)-1, -1, -1):
            #print "x %d" %x
            try:
                index = now.index(no_see[x])
                #print "delete %s at %d of %s" %(no_see[x], index, now)
                no_see = no_see.replace(no_see[x], '')
            except ValueError:
                continue 

        if len(no_see) == 0:
            print "Case #%d: %s" %(i, now)
            break

    if len(no_see) > 0:
        print "Case #%d: INSOMNIA" %(i)
    
