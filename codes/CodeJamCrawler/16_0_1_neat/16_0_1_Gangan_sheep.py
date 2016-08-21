cases=int(input())
for case in range(cases):
	N = int(input())
	if N==0:
		print("Case #"+str(case+1)+": INSOMNIA")
		continue
	p=[]
	i=1
	while True:
		k=i*N
		for a in str(k):
			if a not in p:
				p+=a
		if len(p)==10:
			print("Case #"+str(case+1)+": "+str(k))
			break
		i+=1
		