def solve_case(num):
	if num == 0:
		return -1

	remaining = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	numstr = str(num)
	#max_n = 10 ** len(numstr)

	n = 0
	while len(remaining) > 0:
		n += 1
		num_current = n * num
		numstr_current = str(num_current)

		for char in numstr_current:
			if char in remaining:
				remaining.remove(char)
	
	return num_current