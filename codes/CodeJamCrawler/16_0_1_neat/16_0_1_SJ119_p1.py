output = 'Case #{}: '
need_to_see = {
	'1': True,
	'2': True,
	'3': True,
	'4': True,
	'5': True,
	'6': True,
	'7': True,
	'8': True,
	'9': True,
	'0': True
}

def count_sheep(N):
	if N == 0:
		return 'INSOMNIA'
	n = 0
	not_seen = need_to_see.copy()
	while len(not_seen) > 0:
		n += N
		for c in set(list(str(n))):
			if c in not_seen:
				not_seen.pop(c)
	return n



T = int(raw_input())
for i in xrange(T):
	N = int(raw_input())
	print output.format(i + 1), count_sheep(N)

# for i in xrange(1000000):
# 	print count_sheep(i)