#!/usr/bin/env python3

DEBUG=False

def printStatus(i, c, d):
	s = ''.join([str(i) if d[i] else '-' for i in range(0, 10)])
	
	print("%02d: %5d ..." % (i, c), s)

def addDigits(d, c):
	while True:
		d[c % 10] = True
		if c < 10:
			break
		c //= 10

def calculateDumb(n):
	d = [False] * 10
	c = 0
	i = 0

	while False in d:
		c += n
		i += 1
		addDigits(d, c)
		if DEBUG:
			printStatus(i, c, d)

	return c

def calculate(n):
	if (n == 0):
		return "INSOMNIA"
	else:
		return calculateDumb(n)

t = int(input())
for i in range(1, t + 1):
	r = calculate(int(input()))
	print("Case #{}: {}".format(i, r))
