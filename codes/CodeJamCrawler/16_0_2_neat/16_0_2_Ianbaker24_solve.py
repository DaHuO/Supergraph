import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	stack = in_file.readline().replace('\n', '')
	print "%d %s" % (case, stack)
	moves = 0
	
	while(unsolved(stack)):
		if(stack.find('+') == 0):
			last_plus_prefix = stack.find('-')
			stack = flip(stack, last_plus_prefix)
		else:
			last_minus = stack.rfind('-') + 1
			new_stack = flip(stack, last_minus)
			if((new_stack.rfind('-') + 1) < last_minus):
				stack = new_stack
			else:
				stack = flip(stack, last_minus - 1)
				moves += 1
				stack = flip(stack, last_minus)
		moves += 1
	
	out_file.write(str(moves))
	out_file.write('\n')
	
def unsolved(stack):
	if('-' in stack):
		return True
	else:
		return False
	
def flip(stack, position):
	top_stack = stack[0:position]
	top_stack = top_stack[::-1]
	top_stack = top_stack.replace('-', 'x')
	top_stack = top_stack.replace('+', '-')
	top_stack = top_stack.replace('x', '+')
	return top_stack + stack[position:]
	
if len(sys.argv) != 2:
	print 'Please provide one parameter with the name of the input file location relative to this file.'
else:
	in_file = open(str(sys.argv[1]), 'r')
	out_file = open(str(sys.argv[1]).replace('.in', '.out'), 'w')
	cases = int(in_file.readline())
	case = 0
	while (case < cases):
		solve(in_file, out_file, case)
		case += 1
	in_file.close()
	out_file.close()