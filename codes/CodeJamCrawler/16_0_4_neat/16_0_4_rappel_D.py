fin=open('d_small.in','r')
fout=open('d_small.out','w')

T=int(fin.readline())

for i in range(T):
	temp=fin.readline().split()
	K=int(temp[0])
	C=int(temp[1])
	S=int(temp[2])
	d=K**(C-1)
	s="case #" + str(i+1) + ":"
	for j in range(K):
		s+=" "+str(1+j*d)
	s+="\n"
	fout.write(s)
fin.close()
fout.close()