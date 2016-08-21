def countingSheep(n):
	l = []
	if n == 0:
		return 'INSOMNIA'
	else:
		k = n
		while True:
			for i in str(k):
				if not i in l:
					l.append(i)
			if len(l) == 10:
				return k
			k += n

T = int(raw_input().strip())
for i in range(0, T):
	N = int(raw_input().strip())
	print 'Case #' + str(i+1) + ':', countingSheep(N)