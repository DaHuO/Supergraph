
def run():
	input_file = open('large.in', 'r')
	output_file = open('large.out', 'w')
	first_line = input_file.readline() # read the first line of the content of the small.in file
	T = int(first_line) # convert the string file to integer
	for no in range(1, T+1):
		number = next(input_file)
		const = int(number)
		if (const != 0):
			counter = 0
			mutiplier = 0;
			dic = dict()
			while(counter < 10):
				mutiplier+=1
				number = str(mutiplier * const)
				for key in number:
					if key in dic:
						pass
					else:
						counter += 1
						dic[key] = 1
				
			output_file.write('Case #{}: {}\n'.format(no, number))
		else:
			output_file.write('Case #{}: {}\n'.format(no, "INSOMNIA"))

run()
