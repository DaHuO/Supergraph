import sys

def solve(s):
	result = ""

	for i in range(len(s)):
		if len(result) > 0:
			if result[0] <= s[i]:
				result = s[i] + result
			else:
				result += s[i]

		else:
			result += s[0]

	return result

rl = lambda: sys.stdin.readline()
T = int(rl())

for i in range(T):
	S = str(rl())
	S = S.rstrip('\n')

	result = solve(S)
	print "Case #%d: %s" % (i + 1, result)
