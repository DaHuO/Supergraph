fin=open('a_large.in','r')
fout=open('a_large.out','w')

T=int(fin.readline())

for t in range(T):
	w=fin.readline()
	max=w[0]
	for i in range(1,len(w)):
		if w[i]>=max[0]:
			max=w[i]+max
		else:
			max=max+w[i]
	fout.write("Case #%d: %s" % (t+1, max))

fin.close()
fout.close()