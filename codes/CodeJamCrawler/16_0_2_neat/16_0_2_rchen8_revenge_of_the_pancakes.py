file = open('revenge_of_the_pancakes.txt', 'r')
output = open('revenge_of_the_pancakes_out.txt', 'w')

t = int(file.readline())
for i in xrange(0, t):
	s = file.readline()
	count = 0
	for j in xrange(0, len(s) - 2):
		if s[j] != s[j + 1]:
			count += 1
	if s[-2] == '-':
		count += 1
	output.write('Case #' + str(i + 1) + ': ' + str(count) + '\n')

file.close()
output.close()