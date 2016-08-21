t = int(input())

for _t in range(t):
	n = int(input())
	if n == 0:
		print("Case #{}: {}".format(_t+1,"INSOMNIA"))
		continue
	i = 1
	numbers = [0 for i in range(10)]
	strn = str(n)
	for d in strn:
		numbers[int(d)] = 1
	i += 1
	mask = [1 for i in range(10)]
	while numbers != mask:
		strn = str(n*i)
		for d in strn:
			numbers[int(d)] = 1
		i += 1
	print("Case #{}: {}".format(_t+1,n*(i-1)))