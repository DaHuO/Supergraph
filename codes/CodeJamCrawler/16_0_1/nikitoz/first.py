#!/usr/bin/python
import sets
import sys

f = open(sys.argv[1], 'r')
N = int(f.readline())
for i in range(0, N):
    num = int (f.readline())
    if 0 == num:
        print "Case #" + str(i+1) + ": INSOMNIA"
    else:
	s = set()
	p = 1
        num1 = 0
	while len(s) < 10:
            num1 = num * p
	    for l in str(num1):
                if int(l) not in s:
	       	    s.add(int(l))
	    p = p + 1
        print "Case #" + str(i+1) + ": " + str(num1)

