def prod(a):
	ans=1
	for i in a:
		ans*=i
	return ans
for i in range(int(input())):
	a=[0 for x in range(10)]
	# prod=1
	ans=1
	x=input()
	num=int(x)
	number=num
	for j in range(len(x)):
		a[int(x[j])]+=1
	if x=="0":
		print("Case #"+str(i+1)+": INSOMNIA")
	else:
		while prod(a)==0:
			ans+=1
			num+=number
			x=str(num)
			for j in range(len(x)):
				a[int(x[j])]+=1
			
		print("Case #"+str(i+1)+": "+str(num))

