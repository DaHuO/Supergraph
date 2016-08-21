def check(a):
	flag = False
	count = 0
	#print a
	for i in xrange(len(a)):
		if(a[i]!=0):
			count+=1
	if(count==len(a)):
		return True
	else:
		return False
count = 1
ans = []
for _i in xrange(int(raw_input())):
	n = int(raw_input())
	o = n
	arr = [0 for i in range(10)]
	##print arr
	n1 = str(n)
	flag = 0
	while(True and len(n1)<100000 and o!=0):
		for i in n1:
			arr[int(i)] += 1 
		if(check(arr)==True):
			print "Case #"+str(count)+": " + str(n)
			#ans.append(n)
			flag = 1
			break
		n += o
		n1 = str(n)

	if(o==0):
		#ans.append("INSOMNIA")
		print "Case #"+str(count)+": " + "INSOMNIA"
	count += 1


