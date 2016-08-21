def task1(n):
	seen = set()

	for i in range(1, 10**5):
		digits = list(str(i * n))
		seen = list(seen) + digits
		seen = set(seen)
		if len(seen) == 10:
			return i * n
	return "INSOMNIA"

with open("A-large.in", "r") as f:
	i = 1
	for l in f.read().split("\n")[1:]:
		if len(l) > 0:
			num = int(l)
			print "Case #{}: {}".format(str(i), str(task1(num)))
			i += 1