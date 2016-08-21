testCases = raw_input()
for i in range(int(testCases)):
	inp = raw_input()
	arr = inp.split(" ")
	k   = int(arr[0])
	c   = int(arr[1])
	s   = int(arr[2])
	if s==c and k>s or k<s :
		print "Case #"+str(i+1)+": IMPOSSIBLE"
	if k==s and k==1 :
		print "Case #"+str(i+1)+": "+str(1)
	if k==s and k==2 and c>1:
		print "Case #"+str(i+1)+": "+str(2)
	if k==s and k>1 and c==1 : 
		res = ""
		for j in range(k):
			res+= str(j+1)+" "
		print "Case #"+str(i+1)+": "+res
	if k>2 and k==s and c>1 :
		res = ""
		for j in range(k-1) :
			res += str(2+(k+1)*j)+" "
		print "Case #"+str(i+1)+": "+res
