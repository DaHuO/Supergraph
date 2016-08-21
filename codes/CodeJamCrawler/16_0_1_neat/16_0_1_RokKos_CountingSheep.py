n = int(raw_input())

primer = [str(i) for i in range(10)]
#print primer

for i in range(n):
	st = int(raw_input())
	if(st == 0):
		print "Case #{0}: {1}".format(i+1, "INSOMNIA")
		continue
	arr = [crka for crka in set(str(st))]
	arr = sorted(arr)
	#print "st: " + str(st)
	#print arr
	if(arr == primer):
		print "Case #{0}: {1}".format(i+1, st)
	c = 2
	while True:
		#print "st: " + str(st)
		for t in str(c*st):
			if(t not in arr):
				arr.append(t)

		arr = sorted(arr)
		#print arr
		if(arr == primer):
			print "Case #{0}: {1}".format(i+1, c * st)
			break
		c+=1