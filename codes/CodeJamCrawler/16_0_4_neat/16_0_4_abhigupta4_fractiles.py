#for small
for test in xrange(input()):
	K,C,S = map(int, raw_input().split())
	list1 = [x + 1 for x in xrange(K)]
	temp = ''
	for ele in list1:
		temp += ' '
		temp += str(ele)
	print "Case #" + str(test + 1) + ":" + temp