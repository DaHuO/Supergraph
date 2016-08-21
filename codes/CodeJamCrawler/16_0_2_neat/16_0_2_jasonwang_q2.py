inp = []
filename = raw_input()
f = open(filename)
for line in f:
	inp.append(line.strip())
j = 0
count = 0
n = 0
c = 0
for i in range(1,int(inp[0])+1):
	for j in range(0,len(inp[i])):
		if len(inp[i]) == 1:
			if inp[i] == '-':
				count = 1
			else:
				count = 0
		else:
			if j > 0:
				if inp[i][j] == '-' and inp[i][j-1] == '+':
					count += 2
				if inp[i][j] == '+' and inp[i][j-1] == '-':
					for p in range(0,j):
						if inp[i][p] == '-':
							c += 1
					if c == j:
						count += 1
					c = 0
		if inp[i][j] == '-':
			n += 1
	if n == len(inp[i]):
		count = 1
	print 'Case #' + str(i) + ':',count
	count = 0
	n = 0
	c = 0