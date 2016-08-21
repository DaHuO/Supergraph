def num_of_flips(stack_string):
	stack_string += '+'
	flips = 0
	for i in range(len(stack_string) - 1):
		if stack_string[i] != stack_string[i+1]:
			flips +=1
	return flips

amount_of_inputs = input()
for index in range(amount_of_inputs):
	case_result = num_of_flips(raw_input())
	print("Case #%s: %s" % (index + 1, case_result))
