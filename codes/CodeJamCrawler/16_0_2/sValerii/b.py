INPUT = "b.in"
OUTPUT = "b.out"

def solve(s):
	ans = 0
	current = '+'
	for i in range(len(s)):
		if s[i] != current and s[i] == '-':
			ans += 1
			if i > 0:
				ans += 1
		current = s[i]

	return ans


lines = [line.rstrip('\n') for line in open(INPUT)]
testNum = int(lines[0]);
f = open(OUTPUT, 'w')
for i in range(testNum):
	f.write("Case #%s: %s\n" % (i+1, solve(lines[i+1])))

