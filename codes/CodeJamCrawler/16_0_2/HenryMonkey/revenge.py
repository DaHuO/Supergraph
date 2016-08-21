import sys
input = file(sys.argv[1]).readline

def solution(s):
	pre = s[0]
	ans = 0
	for c in s[1:]:
		if pre != c:
			ans += 1
			pre = c
	if s[-1] == '-':
		ans += 1
	return ans

for case in range(int(input())):
	s = input().strip()
	print "Case #%d: %d " % (case+1, solution(s))

