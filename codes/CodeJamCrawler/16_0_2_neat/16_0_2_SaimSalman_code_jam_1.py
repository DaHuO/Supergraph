import sys

f = open('Input', 'r')
number_of_test_cases = f.readline()

for i in range(0,int(number_of_test_cases)):
	current = f.readline()

	sys.stdout.write("Case #")
	sys.stdout.write(str(i+1))
	sys.stdout.write(": ")

	current_list = []
	isDone = False
	steps = 0

	for i in current:
		if (i != '\n'):
			current_list.append(i)	

	while (len(current_list) != 0):
		count = 1
		isDone = True

		for i in current_list:
			if (i == '-'):
				isDone = 0

		if (isDone == True):
			break


		if (current_list[0] == '-'):
			for i in range(1,len(current_list)):
				if (current_list[i] == '+'):
					break
				else:
					count = count + 1
			for i in range(0, count):
				current_list[i] = '+'
			steps = steps + 1
		elif (current_list[0] == '+'):
			for i in range(1,len(current_list)):
				if (current_list[i] == '-'):
					break
				else:
					count = count + 1
			for i in range(0,count):
				current_list[i] = '-'
			steps = steps + 1
		# break;


	# print current_list
	print steps

