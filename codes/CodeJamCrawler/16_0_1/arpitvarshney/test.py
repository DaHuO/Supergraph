fi = open("A-large.in", "r")
fo = open("f.out","w")
t = int(fi.readline())
for j in range(t):
	n = int(fi.readline())
	count = 2
	s = set(str(n))
	while(len(s)!=10):
		n2=n*count
		s = s.union(set(str(n2)))
		count+=1
		#print(count," ",s)
		if(n2 == n):
			break
	if(len(s)!=10):
		st = "Case #"+str(j+1)+": INSOMNIA\n"
	else:
		st = "Case #"+str(j+1)+": "+str(n2)+"\n"
	#print(n2)
	fo.write(st)
fi.close()
fo.close()
