def problem1Helper(n):
	if n == 0:
		return "INSOMNIA"

	start = n

	nums = [0]* 10

	temp = n
	while temp > 0:
		nums[temp % 10] = 1
		temp = temp // 10

	while 0 in nums:
		n += start
		temp = n
		while temp > 0:
			nums[temp % 10] = 1
			temp = temp // 10
	return n

def problem1():
	data = []
	with open("Problem1Input.txt","r") as file:
		for lines in file:
			if lines[-1] == '\n':
				lines = lines[:-1]
			data += [int(lines)]

	for i in range(1,data[0]+1):
		print "Case #" + str(i) + ": " + str(problem1Helper(data[i]))


problem1()