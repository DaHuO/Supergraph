#!/usr/bin/python
fin = open('B-large.in')
T = int(fin.readline())
for ii in range(T):
	S = fin.readline().strip()
	result = 0
	now = S[0]
	for i in range(len(S)-1):
		k = i + 1
		if now != S[k]:
			result += 1
			now = S[k]
	if S[-1] == '-':
		result += 1
	print "Case #%s: %s" % (ii + 1, result)
fin.close()