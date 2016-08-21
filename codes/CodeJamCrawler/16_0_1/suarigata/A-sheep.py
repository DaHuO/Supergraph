T = int(raw_input())
for t in range(T):
	num=int(raw_input())
	
	if num==0:
		print("Case #" + str(t+1) + ": INSOMNIA")
		continue
	
	check=[0,0,0,0,0,0,0,0,0,0]
	acc=0
	continua=True
	while continua:
		acc+=num
		
		dividido=acc
		while dividido!=0:
			check[dividido%10]=1
			dividido/=10
		
		continua=False
		for che in check:
			if che==0:
				continua=True
				break

	print("Case #" + str(t+1) + ": " + str(acc))
