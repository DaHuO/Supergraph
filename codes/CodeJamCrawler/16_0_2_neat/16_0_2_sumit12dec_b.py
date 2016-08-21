N = input()

test_cases = []
for i in range(0, N):
	test_cases.append(raw_input())

results = []
# test_cases = ['-', '-+', '+-', '+++', '--+-', '+-+++-++++']

def change_sign(stack, till, find_till):
	stack = (till)*find_till + stack[till:]
	return stack


def get_output(stack):

	count = 0
	first_donut_side = stack[0]
	if first_donut_side=='+':
		find_till = '-'
	else:
		find_till = '+'

	while stack != ['+']*len(stack) or ['-']*len(stack):
		till = stack.find(find_till)
		#print till
		if till == -1:
			#print stack
			if stack[0] == '-':
				return count+1
			else:
				return count
		stack = change_sign(stack, till, find_till)
		count+=1
		find_till = '+' if find_till=='-' else '-'
	else:
		#print stack
		if stack[0] == '-':
				return count+1
		else:
				return count




for each_stack in test_cases:
	results.append(get_output(each_stack))

for i in range(0, len(results)):
	print "Case #{0}: {1}".format(i+1, results[i])
