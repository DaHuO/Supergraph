from sets import Set
fin=open("A-large.in.txt",'r')
fout=open("A.out",'w')
tt=int(fin.readline())
for t in range(tt):
	n=int(fin.readline())
	nn=n
	print "Case {0}: {1}".format(t+1,n)
	s=[0,1,2,3,4,5,6,7,8,9]
	for i in str(nn):
		if int(i) in s:
			s.remove(int(i))
	if n!=0:
		while len(s)>0:
			nn+=n
			for i in str(nn):
				if int(i) in s:
					s.remove(int(i))
			if t==1:
				print nn
		fout.write("Case #{0}: {1}\n".format(t+1,nn))
	else:
		fout.write("Case #{0}: INSOMNIA\n".format(t+1))
