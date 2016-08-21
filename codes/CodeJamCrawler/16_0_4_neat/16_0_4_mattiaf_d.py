def solve(k, c, s):
	if k == 1:
		return 1
	if c == 1:
		if s < k:
			return "IMPOSSIBLE"
	
	return ' '.join([str(i) for i in range(1, k+1)])
	
t = int(input())
for cc in range(t):
	k, c, s = [int(x) for x in input().split()]
	print("Case #{}: {}".format(cc+1, solve(k, c, s)))

