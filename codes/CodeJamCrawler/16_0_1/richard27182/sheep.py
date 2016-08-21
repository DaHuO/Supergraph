def lastnumber(n):
	multiplier=1
	alldigitsseen=False
	digitseen=[0,0,0,0,0,0,0,0,0,0]
	while alldigitsseen==False:
		currentnum=multiplier*n
		while currentnum:
			digit=currentnum%10
			digitseen[digit]=1
			currentnum//=10
		if not (0 in digitseen):
			alldigitsseen=True
			return n*multiplier
		multiplier+=1


t = int(input()) 
for i in range(1, t + 1):
	n = int(input())  
	if n==0:
		print("Case #{}: INSOMNIA".format(i))
	else:
		print("Case #{}: {}".format(i,lastnumber(n)))


	
