t = int(raw_input())
for z in xrange(1,t+1):
	v = int(raw_input())
	array = []
	array1 = []
	dic = {}
	print "Case #{}:".format(z),

	for x in xrange(1,2*v):
		array = array + [int(s) for s in raw_input().split(" ")]

	for x in xrange(0,len(array)):
		dic[array[x]] = 0

	for x in xrange(0,len(array)):
		dic[array[x]] = dic[array[x]] + 1

	for x, y in dic.items():
		if y%2 != 0:
			array1.append(x)
	array1.sort()
	for x in xrange(0, len(array1)):
		print array1[x],
	print 