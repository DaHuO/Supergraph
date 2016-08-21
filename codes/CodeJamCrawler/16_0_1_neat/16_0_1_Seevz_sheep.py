T = int(input())

for x in range(T):
	N = int(input())
	num = 0
	digitsSeen = [0 for i in range(10)]

	while 0 in digitsSeen and 100 not in digitsSeen:
		num += N
		digits = [int(i) for i in str(num)]

		for d in digits:
			digitsSeen[d] += 1


	if 100 in digitsSeen:
		print("case #%d: INSOMNIA" % (x+1))
	else:
		print("case #%d: %d" % (x+1, num))
