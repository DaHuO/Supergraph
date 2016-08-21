T = int(raw_input())
for t in range(T):
	N =int(raw_input())
	if N == 0:
		ans = "INSOMNIA"

	else:
		s = [str(i) for i in range(10)]
		c = 0
		while len(s) > 0:
			c+=1
			for a in str(N*c):
				if a in s:
					s.remove(a)
		ans = str(N*c)

	print ("Case #%d: %s" % (t+1, ans))