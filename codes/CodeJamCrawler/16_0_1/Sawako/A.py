for i in range(int(input())):
	n = int(input())
	if n == 0:
		result = "INSOMNIA"
	else:
		required = set()
		seed, j = n, 1
		while(len(required) < 10):
			required |= set(list(map(int, str(n))))
			j += 1
			n = seed * j
		result = n - seed
	print("Case #{}: {}".format(i+1, result))