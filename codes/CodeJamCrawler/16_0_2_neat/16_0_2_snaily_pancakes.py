"""
given stack X with bottommost pancake B with known amount of flips F:

X + needs F flips
X- - needs F flips
+X+- needs
+-Y

"""

with open('pancakes.large') as file:
	cases = int(file.next())
	for case in xrange(cases):
		stack = file.next().strip()
		stack = reduce(lambda cakes, cake: cakes + cake if cake != cakes[-1] else cakes, stack)
		stack = stack.rstrip('+')
		flips = len(stack)
		# flips = 0
		# while stack:
		# 	if stack[0] == '+':
		# 		stack = stack[1:]
		# 		flips = flips + 1
		# 	else:
		# 		stack = ''.join(map(lambda c: {'+': '-', '-': '+'}[c], stack[::-1]))
		# 		flips = flips + 1
		# 	stack = stack.rstrip('+')
		print "Case #%d: %d" % (case + 1, flips)
