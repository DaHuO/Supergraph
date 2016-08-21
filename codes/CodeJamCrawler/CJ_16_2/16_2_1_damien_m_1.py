from collections import Counter
import copy

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
numbers = [Counter(n) for n in numbers]

def possible_numbers(c):
	for i, n in enumerate(numbers):
		c2 = Counter(n)
		for k, v in c2.items():
			if c[k] < v:
				break
		else:
			yield i, n

def solve(case, built=None):
	if case.most_common(1)[0][1] == 0:
		return True, built
	if built is None: built = []
	c = Counter(case)
	for i, n in possible_numbers(c):
		c2 = copy.deepcopy(c)
		c2.subtract(n)
		ok, final = solve(c2, built + [i])
		if ok:
			return ok, final
	return False, []

T = int(input())
for i in range(T):
	inp = input()
	ok, sol = solve(Counter(inp))
	print('Case #{}:'.format(i+1), ''.join(map(str, sol)))