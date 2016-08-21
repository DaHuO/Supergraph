t = int(input())
for i in range(t):
	n = int(input())
	k = n
	if( n == 0):
		print("Case #"+str(i+1)+":","INSOMNIA")
		continue
	digits = set(str(n))
	
	while( len(digits) < 10 ):
		k = k + n
		for j in set(str(k)):
			digits.add(j)
	
	print("Case #",i+1,": ",k,sep = "")