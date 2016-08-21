#!/usr/bin/env python2.7
t = int(raw_input())
for tt in range(t):
	n = int(raw_input())
	if n == 0:
		print "Case #%d: INSOMNIA" % (tt+1)
		continue
	nn = 0
	miss = 10
	exist = [0 for i in range(10)]
	while miss > 0:
		nn += n
		a = nn
		while a > 0:
			if exist[(a%10)] == 0:
				exist[(a%10)] = 1
				miss -= 1
			a /= 10
	print "Case #%d: %d" % (tt+1, nn)
