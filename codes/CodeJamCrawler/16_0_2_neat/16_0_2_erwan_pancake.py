import sys

case_num = 0
for line in sys.stdin:
	if case_num > 0:
		stack = line.rstrip('\n')
		manouvers = 0
		while '-' in stack:
			manouvers += 1
			if '+' not in stack:
				break
			
			if stack[0] == '+':
				t = stack.find('-')
				r = '-'
			else:
				t = stack.find('+')
				r = '+'
			stack = r * t + stack[t:]
				
		print 'Case #%d: %d' % (case_num, manouvers)

	case_num += 1