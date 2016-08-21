def count_sheep(n):
	if n == 0:
		return "INSOMNIA"

	s = set()
	k = n
	while True:
		s.update(str(k))
		if len(s) == 10:
			return k
		k += n
	return i*n

if __name__ == "__main__":
	t = input()

	for i in xrange(1, t+1):
		n = input()
		print "Case #{i}: {result}".format(i=i, result=count_sheep(n))