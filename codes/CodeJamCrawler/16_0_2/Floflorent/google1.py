import sys

with open(sys.argv[1]) as f:
	content = f.read().splitlines()
cases = int(content[0])

for x in xrange(1,cases + 1):
	flip = 0
	stack = str(content[x])
	p = 0

	for i in xrange(0, len(stack)):
		if i == 0 or stack[i] != stack[i - 1]:
			p += 1
		if stack[i] == '-':
			flip = p

	print "Case #" + str(x) + ": " + str(flip)

