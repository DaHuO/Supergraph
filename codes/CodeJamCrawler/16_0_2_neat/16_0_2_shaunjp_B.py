def longest(a):
	count = 0
	b = a[0]
	for i in a:
		if i != b:
			return count
		else:
			count += 1
	return count

def flip(a):
	b = ''
	for i in a:
		if i == '-':
			b += '+'
		else:
			b += '-'
	return b

def getans(a):
	if a == '+':
		return 0
	if a == '-':
		return 1
	count = 0
	while '-' in a:
		b = longest(a)
		a = flip(a[0:b][::-1]) + a[b:]
		count += 1
	return count

a = int(raw_input())

for i in range (1, a + 1):
	b = str(raw_input())
	print "Case #" + str(i) + ": " + str(getans(b))
