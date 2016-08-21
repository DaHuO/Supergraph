for i in range(1,int(input())+1):
	s = input().strip()
	res = s[0]
	for j in range(1,len(s)):
		if res[0] <= s[j]:
			res = s[j] + res
		else:
			res = res + s[j]
	print("Case #"+str(i)+":",res)
