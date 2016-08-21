for t in range(int(input())):
	k,c,s = map(int,input().split())
	print("Case #{0}:".format(t+1),end='')
	for i in range(0,k**c,k**(c-1)):
		print(" {0}".format(i+1),end='')
	print('')
		
		
			
		