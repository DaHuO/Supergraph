__author__ = 'Kenneth'

def printOut(num, out, file):
	file.write("Case #%d: %s\n" % (num, out))
#	print "Case #%d: %d\n" % (num, out)

def find_sleep_time(N):
	digits = {}
	counter = 1

	while True:
		current = counter * N
		while current != 0:
			digit = current % 10
			current /= 10
			digits[digit] = 1

		for i in xrange(0, 10):
			if i not in digits:
				break
			if i == 9:
				return counter * N
		counter += 1

input_file = open('A-large.in')
output_file = open('out-large.txt', 'w')
num_cases = int(input_file.readline())

print 'There are %d cases' % num_cases
for case in xrange(1, num_cases+1):
	N = int(input_file.readline())
	if N==0:
		sleep_time = "INSOMNIA"
	else:
		sleep_time = find_sleep_time(N)

	printOut(case, str(sleep_time), output_file)

input_file.close()
output_file.close()