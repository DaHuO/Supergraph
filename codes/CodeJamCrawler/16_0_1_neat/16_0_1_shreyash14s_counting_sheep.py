def f(n):
	if n == 0:
		return "INSOMNIA"
	d = {str(i):0 for i in range(10)}
	c = 0
	j = 0
	while c <= 9:
		c1 = c
		j += n
		for k in str(j):
			if not d[k]:
				c += 1
				d[k] = 1
		#print(j, c)
		#if c1 == c:
		#	return "INSOMNIA"
	return j

t = int(input())
for i in range(1, t+1):
	n = int(input())
	print("Case #%d:" % i, f(n))
