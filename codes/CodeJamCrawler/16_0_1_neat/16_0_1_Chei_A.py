testcase_count = int(input())
for testcase_index in range(testcase_count):
	N = int(input())
	number = 0
	seen = [False] * 10
	for i in range(1, 1000):
		number = i * N
		for digit in str(number):
			seen[int(digit)] = True
		if (sum(seen) == 10):
			break
	else:
		number = -1
	
	
	
	print("Case #%d: %s" % (testcase_index + 1, number if number >= 0 else "INSOMNIA"))
	
