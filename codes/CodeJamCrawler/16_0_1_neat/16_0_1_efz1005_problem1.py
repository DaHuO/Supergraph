__author__ = "Enric Florit <efz1005@gmail.com>"

def get_digits(N):
	digits = []
	while N > 0:
		digits.append(N % 10)
		N /= 10
	return digits

test_cases = int(raw_input())

solutions = []

for i in xrange(test_cases):
	case = int(raw_input())
	j = 0

	digits = set()

	step = 0
	while len(digits) < 10 and j < 10000:
		j += 1
		step += case

		digits.update(get_digits(step))

	if j == 10000:
		solutions.append(0)
	else:
		solutions.append(step)

for i in xrange(test_cases):
	if solutions[i] == 0:
		print "Case #%d: INSOMNIA" % (i + 1)
	else:
		print "Case #%d: %d" % (i + 1, solutions[i])
