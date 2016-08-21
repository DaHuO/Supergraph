import sys

def get_digit(str):
	if str == 'ZERO':
		return 0
	elif str == 'ONE':
		return 1
	elif str == 'TWO':
		return 2
	elif str == 'THREE':
		return 3
	elif str == 'FOUR':
		return 4
	elif str == 'FIVE':
		return 5
	elif str == 'SIX':
		return 6
	elif str == 'SEVEN':
		return 7
	elif str == 'EIGHT':
		return 8
	elif str == 'NINE':
		return 9
	return -1

def find_del_string(input, str):
	for char in str:
		if char in input:
			input = input.replace(char, '', 1)
		else:
			return 'SAJAL_TEMP'
	return input

def get_string(input):
	op_list = []

	zero = find_del_string(input, 'ZERO')
	while zero != 'SAJAL_TEMP':
		op_list.append(0)
		input = zero
		zero = find_del_string(input, 'ZERO')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])

	two = find_del_string(input, 'TWO')
	while two != 'SAJAL_TEMP':
		op_list.append(2)
		input = two
		two = find_del_string(input, 'TWO')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])

	four = find_del_string(input, 'FOUR')
	while four != 'SAJAL_TEMP':
		op_list.append(4)
		input = four
		four = find_del_string(input, 'FOUR')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])

	six = find_del_string(input, 'SIX')
	while six != 'SAJAL_TEMP':
		op_list.append(6)
		input = six
		six = find_del_string(input, 'SIX')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])

	one = find_del_string(input, 'ONE')
	while one != 'SAJAL_TEMP':
		op_list.append(1)
		input = one
		one = find_del_string(input, 'ONE')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])

	three = find_del_string(input, 'THREE')
	while three != 'SAJAL_TEMP':
		op_list.append(3)
		input = three
		three = find_del_string(input, 'THREE')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])

	five = find_del_string(input, 'FIVE')
	while five != 'SAJAL_TEMP':
		op_list.append(5)
		input = five
		five = find_del_string(input, 'FIVE')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])

	seven = find_del_string(input, 'SEVEN')
	while seven != 'SAJAL_TEMP':
		op_list.append(7)
		input = seven
		seven = find_del_string(input, 'SEVEN')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])

	eight = find_del_string(input, 'EIGHT')
	while eight != 'SAJAL_TEMP':
		op_list.append(8)
		input = eight
		eight = find_del_string(input, 'EIGHT')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])

	nine = find_del_string(input, 'NINE')
	while nine != 'SAJAL_TEMP':
		op_list.append(9)
		input = nine
		nine = find_del_string(input, 'NINE')

	if not input:
		op_list.sort()
		return "".join([str(i) for i in op_list])
	

t = input()
for i in range(t):
	input_str = raw_input()
	print "Case #%d: %s" %(i+1, get_string(input_str))