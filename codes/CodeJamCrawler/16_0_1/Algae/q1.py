import sys

def solve_for(n):
	seen = set()
	for i in range(1, 1000):
		number = str(i * n)
		for x in number:
			seen.add(x)
		if len(seen) == 10:
			return number
	return "INSOMNIA"




lines = sys.stdin.read().split('\n')
test_cases = int(lines[0])

for i in range(1, test_cases+1):
	N = int(lines[i])
	answer = solve_for(N)
	print("Case #{0}: {1}".format(i, answer))