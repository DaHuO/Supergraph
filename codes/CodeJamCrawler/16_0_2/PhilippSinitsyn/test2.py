import sys
from itertools import izip
from collections import deque

# f = sys.stdin
f = open('B-small-attempt1.in')
o = open('testou2-1.out', 'w')
# o = sys.stdout

def ok(stack):
	return sum(stack) == len(stack)

def inverse(stack):
	for i in range(len(stack)):
		stack[i] = int(not stack[i])
	return stack

def flip(stack, count):
	return inverse(stack[count-1::-1]) + stack[count:]

def pankake_bfs(stack):
	qu = deque()
	qu.append((0, stack))
	seen = set([tuple(stack)])
	while True:
		dp, val = qu.popleft()
		if ok(val):
			return dp
		else:
			for c in range(1, len(val) + 1):
				fl = flip(val, c)
				if tuple(fl) not in seen:
					qu.append((dp + 1, flip(val, c)))
					seen.add(tuple(fl))

if __name__ == "__main__":
	total = f.readline()
	
	for i in range(int(total)):
		line = f.readline()
		print i, line
		stack = [s == '+' for s in line[:-1]]
		o.write('Case #%s: %s\n' % (i + 1, pankake_bfs(stack)))
		