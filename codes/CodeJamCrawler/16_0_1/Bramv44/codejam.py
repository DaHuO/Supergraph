t = int(input())  # read a line with a single integer
for i in range(1, t + 1): # loop through all the inputs
	number = int(input()) # read the single integer input
	all_number_str = ''
	for j in range(1, 10000, 1):
		num_str = str(j * number)
		for digit_str in num_str:
			if digit_str not in all_number_str:
				all_number_str += digit_str
		if len(all_number_str) == 10:
			print('Case #' +str(i)+': ' + num_str)
			break
	else:
		print('Case #'+str(i)+': INSOMNIA')