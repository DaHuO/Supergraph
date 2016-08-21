def last_num_before_sleep(first_num):
	if first_num == 0:
		return "INSOMNIA"
	digits = set(map(str, range(10)))
	current_num = 0
	while len(digits) > 0:
		current_num += first_num
		digits = digits.difference([digit for digit in str(current_num)])
	return current_num

amount_of_inputs = input()
for index in range(amount_of_inputs):
	case_result = last_num_before_sleep(input())
	print("Case #%s: %s" % (index + 1, case_result))
