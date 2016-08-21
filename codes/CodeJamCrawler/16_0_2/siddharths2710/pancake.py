t = int(input())
def min(t):
	m = 0
	n = len(t) - 1
	while '-' in t and n >= 0:
		if t[n] == '-':
			for i in range(0,n+1):
				if t[i] == '+':
					t[i] = '-'
				else:
					t[i] = '+'
			m = m + 1
		else:
			n = n - 1
	return m
				
for x in range(t):
	s = []
	c = 0
	j = input()
	for i in j:
		s.append(i)
	if '-' not in s:
		print("Case #",x+1,": 0",sep="")
	else:
		 print("Case #",x+1,": ",min(s),sep="")
