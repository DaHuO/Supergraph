def digit(N):
	return map(int, list(N))

def checkArr(arr):
	for i in arr:
		if i == 0:
			return False
	return True

for t in xrange(1, input()+1):
	N = raw_input()
	org = N
	m = 2
	arr = [0 for _ in xrange(10)]
	if int(N) == 0:
		print "Case #{0}: INSOMNIA".format(t)
	else:
		while True:
			for i in digit(N):
				arr[i] = 1
			if checkArr(arr):
				break
			else:
				N = str(int(org) * m)
				m += 1
		print "Case #{0}: {1}".format(t, N)
					

