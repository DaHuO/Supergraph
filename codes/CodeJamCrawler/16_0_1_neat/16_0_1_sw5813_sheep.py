# Get number of test cases
T = int(raw_input())

# Each test case
for t in range(T):
	N = long(raw_input())
	current_num = N
	checks = [0,1,2,3,4,5,6,7,8,9]
	result = 0
	counter = 0 #hack
	while checks != []:
		number_string = str(current_num)
		for char in number_string:
			if int(char) in checks:
				checks.remove(int(char))
		if checks == []:
			break
		current_num += N
		counter += 1

		# hack to end if not all digits are found
		if counter > 1000:
			current_num = "INSOMNIA"
			break
	result = current_num

	if result == "INSOMNIA":
		print "Case #%d: %s"%(t+1, result)
	else:
		print "Case #%d: %d"%(t+1, result)
