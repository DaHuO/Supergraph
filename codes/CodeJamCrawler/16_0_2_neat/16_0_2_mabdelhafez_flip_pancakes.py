f = open('B-large.in')
num_cases = int(f.readline())


def process(line):
	str_line = str(line)
	if str_line[0] == '-':
		count = -1
	else:
		count = 0
	mode = '+'
	for c in str_line:
		if c == mode:
			continue
		if c == '-':
			count += 2
		mode = c

	if count == -1:
		return 0
	else:
		return count

for i in range(num_cases):
	print "Case #%d: %s" % (i+1, process(f.readline()))



