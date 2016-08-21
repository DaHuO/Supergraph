infile = open("B-large.in", "r")
out = open("output.txt", "w")
for C in xrange(int(infile.readline())):
	a=infile.readline()
	ans,i=0,0
	while a[i]=='-':
		i+=1
		ans=1
	while i < len(a):
		temp=0
		while i < len(a) and a[i]=='+':
			i+=1
			temp=0
		while i < len(a) and a[i]=='-':
			i+=1
			temp=2
		i+=1
		ans+=temp
	out.write("Case #"+str(C+1)+": "+str(ans)+"\n")
infile.close()
out.close()