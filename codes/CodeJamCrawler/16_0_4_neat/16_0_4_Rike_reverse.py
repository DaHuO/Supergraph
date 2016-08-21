file = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\inputs.in", "r")
import math
output = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\output.txt", "w")

num_cases = int(file.readline())

for i in range(num_cases):
	output.write("Case #" + repr(i + 1) + ":")
	input_numbers = file.readline().strip().split()
	
	K = int(input_numbers[0])
	C = int(input_numbers[1])
	S = int(input_numbers[2])
	
	outfilestr = ""
	for i in range(1, K + 1):
		outfilestr = outfilestr + " " + repr(i)
	output.write(outfilestr + "\n")
output.close()
file.close()