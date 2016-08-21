def solve(manesh):
	l = ([bool(c == '+') for c in manesh])
	cur = manesh[0]
	count = 0

	for c in l:
		if cur != c:
			count += 1
			cur = c
	if cur is False:
		count += 1
	return count-1

n = int(input())

for i in range(n):
	inp = str(input())
	print("Case #{}: {}".format(i+1, solve(inp)))
