def flip(string, fr, to):
	count = len(string[fr:to])
	ans = ""
	if string[fr] == "+":
		for k in range(count):
			ans += "-"
	else:
		for k in range(count):
			ans += "+"
	string = ans + string[to:]
	return string


T = int(raw_input())
for i in range(T):
	string = raw_input()
	j = 0
	count = 0
	while(j < len(string)):
		ch = string[j]
		k = j
		while k < len(string) and ch == string[k]:
			k += 1
		if k < len(string):
			string = flip(string, j, k)
			count += 1
			j = 0
		else:
			j += 1
	temp = 0
	for j in string:
		if j == "-":
			temp += 1
	if temp == len(string):
		count += 1
	print "Case #%d: %d" % ((i+1), count)