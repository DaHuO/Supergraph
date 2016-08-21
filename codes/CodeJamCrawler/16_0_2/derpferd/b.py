import sys
from heapq import * 

def put(s):
	sys.stdout.write(s)

def flip(s):
	ns=""
	for c in reversed(s):
		if c == "-":
			ns+="+"
		else:
			ns+="-" 
	return ns


class Node:
	def __init__(self, s):
		self.s = s

	def expand(self):
		ns = []
		for i in range(len(self.s)):
			new_s = flip(self.s[:i+1]) + self.s[i+1:]
			ns += [Node(new_s)]
		return ns

	def done(self):
		return self.s.count("+") == len(self.s)

	def score(self):
		sc = 0
		for i in range(len(self.s)):
			if self.s[i] == "-":
				sc += 2**i
			else:
				sc += -(2**i)
		return abs(sc)

	def __eq__(self, other):
		return other.s == self.s

def search(s):
	ns = []
	vs = set()
	vs.add(s)
	heappush(ns, (0, 0, Node(s)))
	while len(ns):
		ts, score, cur = heappop(ns)
		vs.add(cur.s)
		# print >> sys.stderr, ts, score, cur.s
		if cur.done():
			return ts
		new_ns = cur.expand()
		for n in new_ns:
			if n.s not in vs:
				heappush(ns, (ts+1, n.score(), n))

sys.stdin = open("b.in", "r")
sys.stdout = open("b2.out", "w")

for t in range(int(raw_input())):
	put("Case #" + str(t+1) + ": ")
	print >> sys.stderr, t+1
	s = raw_input()
	ts = search(s)
	put(str(ts) + "\n")
	sys.stdout.flush()

sys.stdout.close()