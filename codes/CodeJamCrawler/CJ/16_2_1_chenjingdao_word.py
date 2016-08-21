#!/usr/bin/python
import sys
f = open('a.in')
l = int(f.readline())
for i in range(l):
	s = f.readline().strip()
	d={}
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	words = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]
	match_letter = ['Z','W','X','G','H','R','F','I','V','O']
	match = [0,2,6,8,3,4,5,9,7,1]
	digits=[]
	count=0
	for j in range(10):
		w = words[match[j]]
		if match_letter[j] in d:
			for k in range(d[match_letter[j]]):
				digits.append(match[j])
				count += len(w)
				for c in w:
					d[c] -= 1
	digits = sorted(digits)
	output=""
	for c in digits:
		output += str(c)
	assert count==len(s)
	for c in d:
		assert d[c]==0
	print 'Case #'+str(i+1)+": "+output
