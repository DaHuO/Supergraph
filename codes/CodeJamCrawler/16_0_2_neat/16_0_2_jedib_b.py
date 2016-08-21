#!/usr/bin/python

nb = int(raw_input())

for n in xrange(1, nb+1):

    pile = raw_input()

    nbFlips = 0
    first = pile[0]
    for i in xrange(1, len(pile)):
		if pile[i] != pile[i-1]:
			nbFlips += 1
    if first == '+':
        if nbFlips % 2 == 1:
            nbFlips += 1
    else:
        if nbFlips % 2 == 0:
            nbFlips += 1

    print "Case #%i: %i" % (n, nbFlips) 

