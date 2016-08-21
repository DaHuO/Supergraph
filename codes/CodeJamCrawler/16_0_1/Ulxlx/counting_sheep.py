#!/usr/bin/env python

t = raw_input()
for i in xrange(1, int(t) + 1):
	n = raw_input()
	ntemp = 0
	nums = [0,0,0,0,0,0,0,0,0,0]
	count = 1
	flag = True
	while 0 in nums:
		if int(n)*count == ntemp:
			print "Case #{}: INSOMNIA".format(i)
			flag = False
			break
		ntemp=int(n)*count
		for num in str(ntemp):
			nums[int(num)] = 1
		count+=1
		ans = ntemp
	if flag == True:
		print "Case #{}: {}".format(i, ans)
  