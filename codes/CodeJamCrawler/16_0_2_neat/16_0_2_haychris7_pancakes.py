import sys
import Queue as Q

class StackState(object):
	def __init__(self, stack, g):
		self.stack = stack
		self.g = g
		self.h = self.get_h()
		self.f = self.g + self.h
	def __lt__(self, other):
		return self.f < other.f
	def __eq__():
		return self.f == other.f

	def get_h(self):
		h = -1
		for i, x in enumerate(self.stack[:-1]):
			h += x != self.stack[i+1]
		return h if h > 0 else 0

	def get_children(self):
		children = []
		for i in range(1,len(self.stack)+1):
			new_stack = self.flip_stack(self.stack, i)
			child = StackState(new_stack, self.g + 1)
			children.append(child)
		return children
	
	def is_goal(self):
		return sum(self.stack) == len(self.stack)

	@staticmethod
	def flip_stack(stack, cut):
		top = reversed(stack[:cut])
		top = [not x for x in top]
		return top + stack[cut:]


T = int(sys.stdin.readline())
for i in range(T):
	initial_stack = sys.stdin.readline().strip()
	stack = [x == '+' for x in list(initial_stack)]
	queue = Q.PriorityQueue()
	seen = set()
	curStack = StackState(stack, 0)
	while not curStack.is_goal():
		for child in curStack.get_children():
			if child not in seen:
				queue.put(child)
				seen.add(child)
		curStack = queue.get()
	answer = curStack.g
	print "Case #%d: %s" % (i+1, answer)
