file = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\inputl.in", "r")

output = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\output.txt", "w")

num_cases = int(file.readline())

for i in range(num_cases):
	output.write("Case #" + repr(i + 1) + ": ")
	stack = file.readline().strip()
	
	if stack[len(stack) - 1] == "+":
		token = "+"
		counter = 0
	else:
		token = "-"
		counter = 1
		
	for idx in range(len(stack)):
		if stack[len(stack) - 1 - idx] != token:
			counter = counter + 1
			if token == "-":
				token = "+"
			else:
				token = "-"
	print(counter)
	output.write(repr(counter) + "\n")
output.close()
file.close()