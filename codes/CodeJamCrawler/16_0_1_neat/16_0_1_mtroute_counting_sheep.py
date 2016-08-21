t = int(input())
for case_n in range(1, t + 1):
	digits = {1,2,3,4,5,6,7,8,9,0}
	n = int(input())
	if n == 0:
		print ("Case #{}: {}".format(case_n, "INSOMNIA"))
	else:
		count = 1
		num = None
		while len(digits) != 0:
			num = n * count
			for digit in str(num):
				digits.discard(int(digit));
			count += 1
		print ("Case #{}: {}".format(case_n, num))