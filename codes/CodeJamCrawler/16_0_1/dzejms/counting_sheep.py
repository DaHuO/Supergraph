t = int(input())  
for i in range(1, t + 1):
	n = int(input())
	digits = set()
	j = 0
	while len(digits) != 10:
		if n == 0:
			break
		j += 1
		num = n * j
		digits.update(str(num))
		#print(len(digits), digits)

	if n == 0:
		print("Case #{}: INSOMNIA".format(i))
	else:
		print("Case #{}: {}".format(i, num))

