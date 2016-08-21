from collections import deque

def solve(S):
	s = deque()
	for l in S:
		if len(s) != 0 and ord(l) >= ord(s[0]):
			s.appendleft(l)
		else:
			s.append(l)
	return s

f = open('A.small.in', 'r')
out = open('A.small.out', 'w')

N = int(f.readline())

for i in xrange(N):
	S = list(f.readline().strip('\n'))
	out.write('Case #{0}: {1}\n'.format(i + 1, ''.join(solve(S))))

f.close()
out.close()