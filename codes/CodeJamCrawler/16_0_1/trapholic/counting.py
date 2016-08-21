def counting(N):
	if not N:
		return 'INSOMNIA'

	digits = set([0,1,2,3,4,5,6,7,8,9])
	i = 1
	num = 0
	while digits:
		num = N*i
		digit_list = set([int(s) for s in str(num)])
		digits = digits - digit_list
		i += 1
	return num

with open('A-large.in') as f:
	content = f.readlines()
	num_of_test = int(content[0])

	with open('output.txt', 'wb') as o:
		for i in range(num_of_test):
			result = counting(int(content[i+1]))
			result_str = 'Case #' + str(i+1) + ': ' + str(result)
			o.write(result_str)
			if i < num_of_test-1:
				o.write('\n')




