f = open('B-large.in', 'r')

s = f.read()

splitted = s.split('\n')

number_cases = int(splitted[0])

out_s = ''

for num in range(0, number_cases):

	case = str(splitted[num + 1])

	count = 0
	if '-' not in case:
		pass
	else:
		prev = case[-1]
		count = 1
		for el in case[::-1]:
			if prev != el:
				prev = el
				count += 1

		last = case[-1]

		if last == '+':
			count -= 1

	out_s += 'Case #%d: %d\n' % (num + 1, count)
		
with open('output.txt', 'w') as f:
	f.write(out_s)