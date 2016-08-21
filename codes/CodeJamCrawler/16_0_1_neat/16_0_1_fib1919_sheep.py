import sys

f = open("A-large.in")

def sheep_solve(n):
	if n == 0:
		return "INSOMNIA"
	cur = n
	dig = [0] * 10
	seen = 0
	br = False
	while 1:
		for c in str(cur):
			if dig[int(c)] == 0:
				seen += 1
				dig[int(c)] = 1
				if seen == 10:
					br = True
		if br:
			break
		cur += n
	return str(cur)

counter = 0

for l in f:
	if counter == 0:
		N = int(l)
		counter += 1
		continue
	print "Case #" + str(counter) + ": " + str(sheep_solve(int(l)))
	counter += 1