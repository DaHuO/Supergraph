T = int(raw_input())
C = 1

while T > 0:
	T -= 1
	X = [False for i in range(10)]

	N = int(raw_input())
	M = N

	if M > 0:
		while M % 10 == 0:
			M = M / 10
			X[0] = True

	print "Case #" + str(C) + ":",
	C += 1

	if M == 0:
		print "INSOMNIA"
	else:
		k = 1
		while True:
			P = k * M
			while P > 0:
				if not X[P % 10]:
					X[P % 10] = True
				P = P / 10
			if not (False in X):
				print str(k * N)
				break
			k += 1