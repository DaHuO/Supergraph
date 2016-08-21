fin=open('b_large.in','r')
fout=open('b_large.out','w')

T=int(fin.readline())

for t in range(T):
	p=fin.readline().rstrip('\n')
	s=0
	for i in range(len(p)-1):
		if p[i]!=p[i+1]:
			s+=1
	fout.write("case #%d: %d\n" % (t+1,s+1 if p[-1]=='-' else s))
fin.close()
fout.close()