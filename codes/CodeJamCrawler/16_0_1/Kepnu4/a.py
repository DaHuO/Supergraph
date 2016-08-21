t = int(input())

for i in range(t):
	n = int(input())

	if n == 0:
		print('Case #%d: INSOMNIA' % (i + 1))  
		continue

	was = [0] * 10
	j = 1
	while 1:
		t = n * j
		while t > 0:
			was[t % 10] = 1
			t //= 10
		if not 0 in was:
			break  
		j += 1
	print('Case #%d: %d' % (i + 1, j * n))