#!/usr/bin/python
import sets
import sys

f = open(sys.argv[1], 'r')
N = int(f.readline())

for t in range(0, N):
    s = list(f.readline().strip())
    l = len(s)
    flips = 0
    i = 1
    finished = False
    while not finished:
        #print s
	while l != i and s[i] == s[0]:
            i = i + 1
	if l <= i:
            if s[0] == '-':
            	flips = flips + 1
	    print "Case #" + str(t+1) +": " + str(flips)
            finished = True
	else:
            flips = flips + 1
	    for j in range(0, i):
        	s[j] = s[i]
            i = i + 1
            
