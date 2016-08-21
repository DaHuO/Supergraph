infile = open('B-large.in', 'r')
outfile = open('pancake_results.txt', 'w')
T = int(infile.readline())
for i in range(T):
	result = 'Case #' + str(i+1) + ': '
	line = infile.readline().strip()
	length = 0
	p = ''
	for c in line:
		if c in ('+', '-') and c != p:
			p = str(c)
			length += 1
	result += str(length-1) if line[-1] == '+' else str(length)
	outfile.write(result + '\n')
infile.close()
outfile.close()