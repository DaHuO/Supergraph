import sys

case_num = 0
for line in sys.stdin:
	if case_num == 0:
		T = int(line.rstrip('\n'))
		case_num += 1
	else:
		N = int(line.rstrip('\n'))
		if N == 0:
			print 'Case #%s: INSOMNIA' % case_num
		else:
			digits = []
			complete = False
			i = 0
			while not complete:
				i += 1
				number = i * N
				digits = list(set(digits + list(str(number))))
				if len(digits) == 10:
					complete = True

			print 'Case #%s: %d' % (case_num, number)
		case_num += 1



