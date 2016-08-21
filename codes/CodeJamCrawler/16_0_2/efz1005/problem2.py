__author__ = "Enric Florit <efz1005@gmail.com>"

def correct_solution(str):
	for i in xrange(len(str)):
		if str[i] == '-':
			return False
	return True

def first_negative(str):
	for i in xrange(len(str)):
		if str[i] == '-':
			return i
	return str('inf')

def last_negative(str):
	last_negative = -1
	for i in xrange(len(str)):
		if str[i] == '+':
			return last_negative
		else:
			last_negative += 1
	return last_negative

test_cases = int(raw_input())
solutions = []

for i in xrange(test_cases):
	case = raw_input()
	j = 0

	while not correct_solution(case):
		j += 1
		if case[0] == '-':
			n = last_negative(case)
			case = '+' * (n + 1) + case[n + 1:]
		else: # case [0] == '+'
			n = first_negative(case)
			case = '-' * (n) + case[n:]

	solutions.append(j)

for i in xrange(test_cases):
	print "Case #%d: %d" % (i + 1, solutions[i])
