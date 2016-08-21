import sys

T = int(sys.stdin.readline())

i = 0
for l in sys.stdin: 
	i += 1
	N = int(l)
	if N == 0:
		print('Case #{}: INSOMNIA'.format(i))
		continue
	s = 0
	seen = set()
	while len(seen) < 10:
		s += N
		for c in str(s):
			seen.add(c)
	print('Case #{}: {}'.format(i, s))
