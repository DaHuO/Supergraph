from collections import Counter

input_file = "A-large.in"

f = open(input_file, 'r')

f.readline()

def case(n):
	seen = Counter()
	
	if n == 0:
		return "INSOMNIA"
	
	i = 0
	while len(seen.values()) < 10:
		for d in str((i + 1) * n):
			seen[d] = 1
		i += 1
	return (i * n)
	
t = 1
for line in f:
	print("Case #{}: {}".format(t, case(int(line))))
	t += 1
