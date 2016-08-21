for tc in range(int(input())):
	s = input()
	a = s[0]
	for i in range(1,len(s)):
		if s[i] >= a[0]:
			a = s[i] + a
#			print(a, S[0])
		else:
			a += s[i]
#			print(a)
	print("Case #%d: %s" %(tc+1, a))
