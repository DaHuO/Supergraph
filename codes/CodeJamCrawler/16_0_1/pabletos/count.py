def count(fileData):

	inputData = open(fileData,'r')
	lines = inputData.readlines()
	N = int(lines[0])
	open('output.txt', 'w').close()
	outputData = open('output.txt', 'a')
	j = 1
	i = 0
	maxim = 10000000
	last_num = 0

	while j <= N:

		i += 1
		list_num = set()
		number = int(lines[i])
		for x in range(1,maxim):
			next_number = str(x*number)
			for n in next_number:
				list_num.add(int(n))
			if(len(list_num) == 10):
				last_num = next_number
				break
		if (last_num == 0):
			last_num = 'INSOMNIA'
		print('case #{0}: {1}'.format(j,last_num))
		outputData.write('case #{0}: {1}\n'.format(j,last_num))
		j += 1

count('A-large.in')
