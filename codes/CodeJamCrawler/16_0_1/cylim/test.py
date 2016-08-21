t = int(input())  
matched = [int(i) for i in '0123456789']
for i in range(1, t + 1):
	num = int(input())
	match = []
	match += map(int, str(num))

	for n in range(1, 100):
		lastNumber = n * num
		match += map(int, str(lastNumber))
		match = list(set(match))

		if match == matched:
			print("Case #{}: {}".format(i, lastNumber))
			break
	
	if match != matched:
		print("Case #{}: {}".format(i, "INSOMNIA"))
	