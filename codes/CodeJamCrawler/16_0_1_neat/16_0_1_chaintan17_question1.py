#!/usr/bin/env python
# -*- coding: utf-8 -*-
# c = [c for c in "1234"]
# print c
# exit()

__author__ = 'por'

f = open('1.in', 'r')
o = open('1.out', 'w')
T = int(f.readline().strip())

for t in xrange(T):
	# (n, m, o) = map(int, f.readline().strip().split(' '))
	l = int(f.readline().strip())
	sleepWell = True
	n = 1
	uniqueNumber = []
	countRepeat = 0
	prevLen = 0
	lastDigit = ""
	while sleepWell:
		number = n * l
		uniqueNumber = uniqueNumber + [c for c in str(number)]
		uniqueNumber = list(set(uniqueNumber))
		newLen = len(uniqueNumber)
		n = n + 1
		if newLen == 10:
			sleepWell = False
			lastDigit = number
		elif newLen == prevLen and countRepeat > 100:
			sleepWell = False
		else:
			sleepWell = True
			countRepeat = countRepeat + 1
			prevLen = newLen

	if lastDigit != "":
		s = "Case #%d: %s\n" % (t+1, lastDigit)
	else:
		s = "Case #%d: INSOMNIA\n" % (t+1)
	print s
	o.write(s)
    #
	# res = str(n) + str(m) + str(o) + l
	# s = "Case #%d: %s\n" % (t+1, res)
	# print s