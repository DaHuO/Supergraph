for i in range(int(input())):
	s = input()
	mx = s[0]
	for k in range(1, len(s)):
		c = mx + s[k]
		d = s[k] + mx
		if c > d :
			mx = mx + s[k]
		else:
			mx =  s[k] + mx
	print("Case #%d: %s" %(i+1 , mx))