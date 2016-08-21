T = int(input())
for t in range(T):
	n = int(input())
	seen = {str(i): 0 for i in range(10)}
	d = 0
	ans = -1
	iteration = 0
	while iteration < 10000:
		iteration += 1
		d += n
		for i in str(d):
			seen[i] = 1
		if(sum([seen[v] for v in seen]) == 10):
			ans = d
			break
	if(ans == -1):
		print("Case #{}: INSOMNIA".format(t+1))
	else:
		print("Case #{}: {}".format(t+1, ans))

