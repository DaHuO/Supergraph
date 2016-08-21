t = input()
i = 1
while i <= t:
	n = input()
	if n == 0:
		print("Case #{}: INSOMNIA".format(i))
		i = i + 1
		continue
	hash = [0] * 10
	j = 1
	while True:
		x = n * j
		j = j + 1
		num = x
		while x > 0:
			m = x % 10
			x = x / 10
			hash[m] = hash[m] + 1;
		if hash[0] >= 1 and hash[1] >= 1 and hash[2] >= 1 and hash[3] >= 1 and hash[4] >= 1 and hash[5] >= 1 and hash[6] >= 1 and hash[7] >= 1 and hash[8] >= 1 and hash[9] >= 1:
			break
	print("Case #{}: {}".format(i, num))
	i = i + 1