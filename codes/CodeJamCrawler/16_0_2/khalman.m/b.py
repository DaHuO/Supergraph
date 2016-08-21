data = []
f = open('input.txt', 'r')
f.readline()
for line in f:
	data.append(line[:-1])

#print data

for (test_id, s) in enumerate(data):
	if len(s) == 0:
		break
	s = s + '+'
	prev = s[0]
	counter = 0
	for c in s[1:]:
		if prev != c:
			counter += 1
		prev = c
	print 'Case #{}: {}'.format(test_id + 1, counter)