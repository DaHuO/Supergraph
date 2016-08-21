def solve(d):
	if d == 0:
		return 'INSOMNIA'
	seen = set()
	i = 1
	while True:
		n = d * i
		while n > 0:
			seen.add(n % 10)
			n /= 10
		if len(seen) == 10:
			return i * d
		i += 1

f = open('A.in', 'r')
out = open('A.out', 'w')

N = int(f.readline())

for i in xrange(N):
	d = int(f.readline())
	out.write('Case #{0}: {1}\n'.format(i + 1, solve(d)))

f.close()
out.close()