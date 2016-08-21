t = int(raw_input())
for _ in range(t):
	k,c,s = map(int,raw_input().split())
	ans = []
	mul = k**(c-1)
	j = 1
	for i in range(s):
		ans.append(j)
		j = j + mul
	ans = [str(i) for i in ans]
	print("Case #%i: %s" % (_+1, " ".join(ans)))