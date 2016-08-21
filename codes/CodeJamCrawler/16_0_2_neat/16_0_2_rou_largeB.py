#!/usr/bin/python

cases = int(raw_input())
for case in xrange(1, cases+1): 
	pancakes = raw_input()
	bits = [True if pancake == '+' else False for pancake in pancakes]
	flips = 0 

	while True: 
		while bits and bits[-1] == True: 
			bits.pop()
		if not bits: 
			break
		
		firstFalse = bits.index(False)
		if firstFalse != 0:
			flips += 1
			for b in xrange(0, firstFalse): 
				bits[b] = False

		flips += 1
		bits = [not(bit) for bit in reversed(bits)]
		
	print "Case #%d: %d" % (case, flips)
