for t in range(int(input())):
	n = int(input())
	if n == 0:
		ans = "INSOMNIA"
	else:
		flag = {}
		i = 0
		while len(flag)<10:
			i += n
			for c in str(i):
				flag[c] = 1
		ans = i
	print("Case #{0}: {1}".format(t+1,ans))
			
		