f=open("input.txt")
t=int(f.readline())
f2 = open('out2.txt', 'w')


for i in range(t):
	s=f.readline()
	if(len(s)==1):
		f2.write("Case #"+str(i+1)+": "+s)
		continue
	k=""
	for j in s:
		if k=="":
			k=j
		else:
			st=k[0]
			en=k[-1]
			if j>=st:
				k=j+k
			else:
				k=k+j
	f2.write("Case #"+str(i+1)+": "+k)
f.close()
f2.close()

