n = int(input())
for i in range(n):
	print("Case #%d: " % (i+1), end = "")
	s = input()
	k = ""
	k = s[0]
	for c in s[1:]:
		if k[0] <= c:
			k = c + k
		else:
			k = k + c

	print(k)