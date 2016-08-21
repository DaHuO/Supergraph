file = open('A-large.in')
num_of_cases = int(file.readline())
output_file = open('output1.txt', 'w')

for case in range(1,num_of_cases+1):
	value = file.readline()
	check = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, }

	if int(value) != 0:
		for digit in value:
			check[digit] = 1

		i = 1
		mult = ''
		while(len(set(check.values()))!=1):
			i += 1
			mult = str(long(value)*i)
			for digit in mult:
				check[digit] = 1

		print >> output_file, "Case #%d: %s" % (case, mult)

	else:
		print >> output_file, "Case #%d: INSOMNIA" % (case)


