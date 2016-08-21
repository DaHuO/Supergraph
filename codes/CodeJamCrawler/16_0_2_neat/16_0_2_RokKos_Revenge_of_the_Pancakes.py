def check(lst):
	for state in lst:
		if(not state):
			return False

	return True

t = int(raw_input())

for i in range(t):
	s = raw_input()
	#print s
	arr = []
	for chr in s:
		if(chr == "+"):
			arr.append(True)
		else:
			arr.append(False)

	if(check(arr)):
		print "Case #{0}: {1}".format(i+1, 0)
		continue

	if(len(arr) == 1):
		print "Case #{0}: {1}".format(i+1, 1)
		continue


	tr = arr[0]
	c = 1
	while True:
		fl = True
		for j in range(0, len(arr)):
			if(arr[j] != tr):
				#print arr
				tr = arr[j]
				fl = False
				for k in range(0,j):
					#print k
					arr[k] = not arr[k]
				arr[0:j] = arr[0:j][::-1]
				#print arr
				break

		if(fl):
			for k in range(0,len(arr)):
				#print k
				arr[k] = not arr[k]
			arr[0:j] = arr[0:j][::-1]
			#print arr			

		if(check(arr)):
			print "Case #{0}: {1}".format(i+1, c)
			break
		c+=1
		#print "----------------" + str(c)