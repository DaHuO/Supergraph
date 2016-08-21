def flip(s, n):
	substr = list(s[n:][::-1])
	for i in range(len(substr)):
		if substr[i] == '+':
			substr[i] = '-'
		else:
			substr[i] = '+'
	return s[:n] + ''.join(substr)

def solve(s):
	s = s[::-1]
	flips = 0
	if s[0] !='+':
		flips += 1
	old = s[0]
	for c in s[1:]:
		if c!=old:
			flips+=1
		old = c
	return flips

items = []
n = int(raw_input())
for i in range(n):
	items.append(raw_input())

i = 1
for item in items:
	print "Case #%d: %d" % (i,solve(item))
	i += 1