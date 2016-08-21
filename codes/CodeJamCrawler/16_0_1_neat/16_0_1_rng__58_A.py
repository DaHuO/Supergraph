def func(N):
	a = [0] * 10
	x = 0
	cnt = 0
	
	while True:
		x = x + N
		y = x
		while y > 0:
			if a[y % 10] == 0:
				a[y % 10] = 1
				cnt = cnt + 1
			y = y / 10
		if cnt == 10:
			return x

T = input()

for t in range(T):
	N = input()
	if N == 0:
		print "Case #" + str(t + 1) + ": " + "INSOMNIA"
	else:
		print "Case #" + str(t + 1) + ": " + str(func(N))
