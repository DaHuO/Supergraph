def fliprev(s,i):
	str = ""
	for j in range(i):
		if s[j] == "+":
			str = str + "-"
		else:
			str = str + "+"
	str = str[::-1]
	str = str + s[i:]
	return str



T = int(raw_input())
for i in range(T):
	a = raw_input()
	count = 0
	j=0
	while j<len(a):
		ch = a[0]
		k=0
		while (k<len(a) and ch==a[k]):
			k = k + 1
		if k < len(a):
			a = fliprev(a,k)
			count = count + 1
			j = 0
		else:
			j = j + 1
	#check if all blank
	c=0
	for j in range(len(a)):
		if a[j] == "-":
			c += 1
	if c == len(a):
		count += 1

	print "Case #" + str(i+1) + ": " + str(count)


