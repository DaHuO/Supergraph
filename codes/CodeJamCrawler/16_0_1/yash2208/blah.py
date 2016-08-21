infile = open("A-large.in", "r")
out = open("output.txt", "w")
A = int(infile.readline())
for C in xrange(A):
	a=['0','1','2','3','4','5','6','7','8','9']
	n=int(infile.readline())
	if n == 0:
		ans="INSOMNIA"
	else:
		i=1
		while a:
			temp=i*n
			nc=list(str(temp))
			i+=1
			for x in nc:
				if x in a: a.remove(x)
		ans = str(temp)
	out.write("Case #"+str(C+1)+": "+ans+"\n")
infile.close()
out.close()