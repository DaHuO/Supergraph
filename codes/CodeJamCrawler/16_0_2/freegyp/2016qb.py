fin=open("B-large.in.txt",'r')
fout=open("B.out",'w')
tt=int(fin.readline())
for t in range(tt):
	ss=fin.readline()
	print ss
	s=[i for i in ss if i=='-' or i=='+']
	countchange=0
	for i in range(len(s)-1):
		if s[i]!=s[i+1]:
			countchange+=1
	if s[-1]=='-':
		countchange+=1
	fout.write("Case #{0}: {1}\n".format(t+1,countchange))
