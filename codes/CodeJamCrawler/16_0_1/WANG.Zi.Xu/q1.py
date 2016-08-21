num = input()
for case in range(1, num + 1):
	print "Case #{}:".format(case),
	n = input()
	if n == 0:
		print "INSOMNIA"
	else:
		d = [False for i in range(10)]
		done = False
		t = n
		while not done:
			m = t
			while t != 0:
				d[t % 10] = True
				t /= 10
			done = True
			for i in d:
				if not i:
					done = False
					break
			t = m + n
		print t - n
