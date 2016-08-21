file = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\inputl.in", "r")

output = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\output.txt", "w")

num_cases = int(file.readline())
		

for i in range(num_cases):
	output.write("Case #" + repr(i + 1) + ": ")
	number = int(file.readline().strip())
	
	if number == 0:
		output.write("INSOMNIA\n")
		continue
	
	cur_number = number
	seen_numbers = set()
	counter = 0
	
	while(seen_numbers != set([i for i in range(10)])):
		for i in repr(cur_number):
			seen_numbers.add(int(i))
		cur_number = cur_number + number
		counter = counter + 1

	#print(counter * number)
	output.write(repr(counter * number) + "\n")
output.close()
file.close()