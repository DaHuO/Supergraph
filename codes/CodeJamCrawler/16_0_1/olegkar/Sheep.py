def sheep(number):

	my_list = []
	counter = 1
	
	if number == 0:
		return "Insomnia"
	else:
		while len(my_list) < 10:
			#print len(my_list)
			newnumber = number*counter
			number_str = str(newnumber)
			for digit in number_str:
				if not digit in my_list:
					#print counter
					my_list.append(digit)
			counter = counter + 1
		return newnumber
				

# print sheep(1692)
with open("A-large.in", "r+") as input:
	file_list = input.readlines()
with open("output_file.txt","w") as output:
	for i in range (1,len(file_list)):
		a = sheep(int(file_list[i]))
		output.write("Case #" + str(i) + ": " + str(a) + "\n")