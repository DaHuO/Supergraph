def part1a():
	file = open('A-large.in')
	num_of_cases = file.readline()
	output_file = open('output.txt', 'w')
	i = 1
	while i < int(num_of_cases) + 1:
		number = file.readline()
		inputs = {'0':False, '1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False}
		j = 1
		if long(number) !=0:
			count = 0
			while True:	
				count = 0
				for k in inputs.values():
					if k == True:
						count = count + 1
				if count == 10:
					break
				print count
				print inputs
				number1 = str(j * long(number))
				for x in number1:
					inputs[x] = True
				j = j + 1
				
			print i	
			print >> output_file, "Case #%d: %s" % (i, number1)
		else:
			print  >> output_file, "Case #%d: INSOMNIA" % (i)

		i = i + 1

if __name__ == "__main__":
	part1a()