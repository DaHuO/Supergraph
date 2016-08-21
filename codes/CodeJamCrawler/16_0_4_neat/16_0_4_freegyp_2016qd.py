fin=open("D-small-attempt2.in.txt",'r')
fout=open("D.out",'w')
tt=int(fin.readline())
for t in range(tt):
	l=fin.readline().split()
	k,c,s=int(l[0]),int(l[1]),int(l[2])
	fout.write("Case #{0}:".format(t+1))
	for i in range(k):
		fout.write(" {0}".format(i+1))
	fout.write("\n")
#	if c==1:
#		if s<k:
#			fout.write(" IMPOSSIBLE\n")
#		else:
#			for i in range(1,k+1):
#				fout.write(" {0}".format(i))
#			fout.write("\n")
#	elif s<k/2+k%2:
#		fout.write(" IMPOSSIBLE\n")
#	else:
#		if k==1:
#			fout.write(" {0}".format(k))
#		for i in range(2,k*k+1,2*k+1):
#			fout.write(" {0}".format(i))
#		fout.write("\n")
