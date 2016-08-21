t = int(input())
for i in range(t):
	k, c, s = map(int, input().split())
	ans = "Case #%d:" % (i + 1)
	for j in range(s):
		ans += " %d" % (j + 1)
	
	print(ans)
