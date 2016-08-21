import sys

nt, *n = map(int, sys.stdin.readlines())


def digits_set(i):
	return set(str(i))


for it in range(nt):
	if n[it]:
		i = n[it]
		seen = digits_set(i)
		while (len(seen) < 10):
			i += n[it]
			seen.update(digits_set(i))
	else:
		i = 'INSOMNIA'
	print('Case #{}: {}'.format(it + 1, i))
