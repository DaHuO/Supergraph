from sys import stdin
cin = lambda: int(stdin.readline().strip('\n\r '))

n = cin()
data = []
for i in range(n):
	data.append(cin())

for i in range(n):
	if data[i] == 0:
		print "Case #%i: INSOMNIA" % (i + 1)
	else:
		s = 0
		visited = [False] * 10
		while False in visited:
			s += data[i]
			for ch in str(s):
				visited[int(ch)] = True
		
		print "Case #%i: %i" % (i + 1, s)