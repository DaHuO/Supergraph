t = int(input())
for caseno in range(1,t+1):
	n = int(input())
	d = {}
	if(n==0):
		print("Case #%d: INSOMNIA"%(caseno))
		continue	
	ans=0
	while(len(d)<10):
		ans+= n
		temp = ans
		while(temp>0):
			d[temp%10] = True
#			d.append(temp%10,True)
			temp//=10
	print("Case #%d: %d"%(caseno,ans))
