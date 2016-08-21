from sys import stdin, stdout
t = int(stdin.readline())
for i in range(1, t+1):
	s = stdin.readline().strip()
	c = s[0]
	a = 1
	for j in range(1, len(s)):
		if s[j] != c:
			a += 1
			c = s[j]
	if s[-1] == '+':
		a -= 1
	stdout.write('Case #'+str(i)+': '+str(a)+'\n')