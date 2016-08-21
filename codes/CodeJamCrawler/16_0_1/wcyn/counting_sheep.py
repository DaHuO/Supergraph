def count_sheep(filename_in, filename_out):
	with open(filename_in, 'r') as input_f:
		test_cases = int(input_f.readline());
		all_digits = []
		[all_digits.append(str(i)) for i in range(10)]
		all_digits = set(all_digits)
		for x in range(test_cases):
			n = input_f.readline().replace('\n','')
			print n
			num_array = []
			i = 1
			last_num = n
			if int(n) == 0:
				print "n is zero"
				last_num = "INSOMNIA"
			else:
				while(all_digits.difference(num_array)):
					last_num = str(i * int(n))
					num_array += list(last_num)
					i += 1
			mode = 'a'			
			with open(filename_out,mode) as output_f:
				output_f.write('Case #%d: %s\n' %(x+1,last_num))

count_sheep('A-large.in', 'A-large.out')
 