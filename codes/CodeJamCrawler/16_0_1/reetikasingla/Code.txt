t=int(input())
for i in range(t):
	number=int(input())
	setA=set([])
	for j in range(1,100):
		if(number==0):
			break
		result=number*j
		setB=set(list(str(result)))
		setA=setA.union(setB)
		if(len(setA)==10):
			break
	if(len(setA)==10):
		print("Case #"+str(i+1)+": "+str(result))
	else:
		print("Case #"+str(i+1)+": "+"INSOMNIA")