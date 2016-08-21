for t in range(int(input())):
	n = input() + '+'
	ans = 0
	for i, j in zip(n, n[1:]):
		if i!=j: ans+=1
	print("Case #{0}: {1}".format(t+1,ans))
			
		