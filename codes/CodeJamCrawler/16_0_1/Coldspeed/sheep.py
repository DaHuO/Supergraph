 #a = (11111111, 2)

for t in range(int(input())):
	i = 1
	N = int(input())
	if(N == 0):
		print("Case #%d: INSOMNIA" %(t+1))
		continue
	a = 0
	while(1):
	    temp = N * i
	    while(temp > 0):
	    	a = a | (1 << (temp%10))
	    	temp//=10
	    if a==1023: break
	    i += 1

	print("Case #%d: %d" %(t+1, N*i))	
