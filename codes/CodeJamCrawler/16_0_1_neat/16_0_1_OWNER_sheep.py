t = int(input())

for i in range(t):
	array = [0]*10
	n = int(input())
	j = 1;
	if n==0:
		string = "Case #"+str(i+1)+": INSOMNIA"
		print string
		continue
	while sum(array)<10:
		temp = n*j 
		while temp>=10:
			r = temp%10
			array[r]=1
			temp = temp/10
		array[temp]=1
		j = j + 1
	string = "Case #"+str(i+1)+": "+str(n*(j-1))
	print string