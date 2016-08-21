#!/bin/python

def AllDigitsFound(d):
	r=True
	for b in d:
		r = r and b
	return r

def SplitDigits(n):
	result=[]
	while n != 0:
		result.append(n%10)
		n/=10
	return result

def CountSheep(n):
	digits=[False]*10
	count = 1
	while not AllDigitsFound(digits) and count < 100000:
		num = n * count
		numdigits = SplitDigits(num)
		for d in numdigits:
			digits[d]=True
		# print digits
		count+=1
	if AllDigitsFound(digits):
		return num
	else:
		return "INSOMNIA"

t = int(raw_input())

for i in xrange(1, t + 1):
	n = int(raw_input())
	if n == 0:
		o = "INSOMNIA"
	else:
		o = CountSheep(n)
	print "Case #{}: {}".format(i, o)