from sys import stdin
cin = lambda: stdin.readline().strip('\n\r ')

def flip(s, n):
	top = s[:n]
	bottom = s[n:]
	new = ""
	
	for ch in top:
		if ch == '-':
			new += '+'
		else:
			new += '-'
	
	return new[::-1] + bottom

t = int(cin())
data = []

for i in range(t):
	data.append(cin())

for i in range(t):
	line = data[i]
	c = 0
	
	while '-' in line:			
		top = line[0]
		for j in range(len(line)):
			if line[j] != top:
				line = flip(line, j)
				break
		else:
			line = flip(line, len(line))

		c += 1
	
	print "Case #%i: %i" % (i + 1, c)