#!/usr/bin/python
t = int(raw_input())
i = 1
while i <=t:
	s = raw_input()
	n = ""
	f = ""
	for j in s:
		if n == "":
			n = j
			f = j
		elif f > j:
			n = n + j
		else:
			n = j + n
			f = j
	print "Case #%d: %s" %(i, n)
	i+=1
