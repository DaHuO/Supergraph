import collections
import random

T = int(input())

def endcount(s):
	c = 0
	for i in range(len(s) - 1, -1, -1):
		if s[i] == '-':
			return c
		c += 1
	return c

def soln_old(inp):
	queue = collections.deque()
	queue.append((inp, 0))
	seen = set()
	while len(queue) > 0:
		c, d = queue.popleft()
		# print(d, c)
		# if d > 4:
			# break
		if c == '+' * len(c):
			# print('Case #{}: {}'.format(t, d))
			break
		for i in range(1, len(c) + 1):
			f = c[:i][::-1].replace('+', '.').replace('-', '+').replace('.', '-') + c[i:]
			if f not in seen:
				seen.add(f)
				queue.append((f, d + 1))
	return d

def swapchars(s):
	o = ''
	for i in range(len(s)):
		o += '+' if s[i] == '-' else '-'
	return o

def startcount(stack, char):
	for i in range(len(stack)):
		if stack[i] != char:
			return i
	return len(stack)

def soln_new(stack):
	flips = 0
	count = startcount(stack, stack[0])
	while count < len(stack) or stack[0] != '+':
		stack = count * ('+' if stack[0] == '-' else '-') + stack[count:]
		count = startcount(stack, stack[0])
		flips += 1
	return flips

for t in range(1, T + 1):

	inp = input()

	# inp = ''.join(random.choice('+-') for i in range(8))
	n = soln_new(inp)
	# o = soln_old(inp)
	print('Case #{}: {}'.format(t, n))
	# print(n, o)

	
