from Queue import deque
def solve():
	T = int(raw_input())
	for t in xrange(1,T+1):
		S = list(raw_input())
		l = len(S)
		q = deque([S[0]])
		for i in xrange(1,l):
			if S[i] >= q[0]:
				q.appendleft(S[i])
			else:
				q.append(S[i])
		print "Case #%d: %s" % (t,"".join(q))
solve()