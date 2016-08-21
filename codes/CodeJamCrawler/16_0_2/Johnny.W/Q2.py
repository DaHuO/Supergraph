def simplify(cakes):
	res = [cakes[0]]
	last = cakes[0]
	for c in cakes[1:]:
		if c != last:
			res.append(c)
			last = c
	if res[-1] == '+':
		res = res[:-1]
	return res

def solve(cakes):
	return len(cakes)

T = input()
for c in xrange(1, T + 1):
	cakes = list(raw_input())
	cakes = simplify(cakes)
	# print cakes
	res = solve(cakes)
	print "Case #%d: %d"% (c, res)