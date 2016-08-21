T = input()

cas = 0

while T > 0:

	T -= 1
	cas += 1
	print "Case #%d:" % cas, 
	N = input()

	if N == 0:
		print "INSOMNIA"
	else:

		vis = [0 for _ in xrange(10)]
		for i in xrange(1, 1000000):

			t = i * N
			while t > 0:
				vis[t % 10] = 1
				t /= 10

			finished = True
			for x in range(10):
				if vis[x] == 0:
					finished = False
					break

			if finished:
				print i * N
				break
