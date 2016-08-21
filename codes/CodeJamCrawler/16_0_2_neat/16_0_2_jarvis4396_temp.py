text_file = open("output.txt", "w")
lines = [line.rstrip('\n') for line in open('input.txt')]
t = int(lines[0])
for k in range(1,t+1):
	s = lines[k]
	a = []
	for i in range(0,len(s)):
		if(s[i] == '+'):
			a.append(1)
		else:
			a.append(0)
	c = 0
	while (1):
		if(sum(a) == len(a)):
			break

		l = -1
		for i in range(1,len(a)):
			if(a[i-1] != a[i]):
				l = i
				break

		if(l == -1):
			l = len(a)

		for j in range(0,l):
			a[j] = int(not a[j])
		c = c + 1

	text_file.write('Case #' + str(k) + ': ' + str(c) + '\n')
text_file.close()