T = int(raw_input())

def solve():
	s = raw_input()
	s = s.rstrip('+')
	now = '-'
	ans = 0
	while s:
		ans += 1
		s = s.rstrip(now)
		now = '+' if now == '-' else '-'
	print ans

for i in range(1, T + 1):
	print "Case #%d:" % i,
	solve()