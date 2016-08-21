t=int(input())
for t0 in range(t):
	n=int(input())
	allDigits=[0,1,2,3,4,5,6,7,8,9]
	numseen=[]
	i=1
	n1=0


	while numseen[:]!=allDigits[:] and n!=0:
		n1=n*i
		n1=str(n1)		
	
		for j in range(len(n1)):
			numseen.append(int(n1[j]))
		numseen = list(set(numseen))
		numseen = sorted(numseen)
		n1=int(n1)
		i+=1
	if n1==0: print("Case #"+str(t0+1)+": INSOMNIA")
	else: print("Case #"+str(t0+1)+": "+str(n1))	

