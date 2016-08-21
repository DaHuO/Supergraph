t=int(input())
answer={0,1,2,3,4,5,6,7,8,9}
boolean=False
j=0
for i in range(t):
	j+=1
	ans=str("Case #"+str(j)+":")
	n=int(input())
	if(n==0):
		print(ans,"Insomnia")
	else:
		numbers=set()
		i=1
		while True:
			num=n*i
			dig=list(int(d) for d in str(num))
			numbers.update(dig)
			if(numbers==answer):
				print(ans,n*i)
				boolean=True
				break
			i+=1
		if(not boolean):
			print("Insomnia")
