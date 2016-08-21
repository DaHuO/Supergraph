def sleep_sheep(n, i=1, numbers='0123456789', result=0):
	if numbers == '':
		return result
	n_str = str(n*i)
	numbers = filter(lambda x: x not in n_str, numbers)
	return sleep_sheep(n, i+1, numbers, n*i)

input = open('A-large.in', 'r')
output = open('output.txt', 'w')
output.seek(0)
output.truncate()
T = int(input.readline())
case = 0
for i, line in enumerate(input):
	N = int(line)
	if case < T:
		if N == 0:
			sleep = 'INSOMNIA'
		else:
			sleep = str(sleep_sheep(n=N))

		case = case + 1
		print "Case #%d: %s" % (case, sleep)
		output.write("Case #%d: %s\n" % (case, sleep))
print 'Finish'
output.close()
input.close()