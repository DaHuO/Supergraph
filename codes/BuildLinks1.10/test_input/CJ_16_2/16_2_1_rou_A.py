#!/usr/bin/python
from collections import Counter

cases = int(raw_input())
for case in xrange(1, cases+1): 
	raw = raw_input()
	letters = Counter(raw)

	c0 = letters['Z']
	c2 = letters['W']
	c4 = letters['U']
	c6 = letters['X']
	c8 = letters['G']
	letters.subtract(Counter(c0*"ZERO" + c2*"TWO" + c4*"FOUR" + c6*"SIX" + c8*"EIGHT"))
	
	c1 = letters['O']
	c3 = letters['H']
	c5 = letters['F']
	c7 = letters['S']
	letters.subtract(Counter(c1*"ONE" + c3*"THREE" + c5*"FIVE" + c7*"SEVEN"))

	c9 = letters['E']

	tel = c0*'0' + c1*'1' + c2*'2' + c3*'3' + c4*'4' + c5*'5' + c6*'6' + c7*'7' + c8*'8' + c9*'9'
	print "Case #%d: %s" % (case, tel)
