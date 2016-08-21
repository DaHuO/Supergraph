import os

input_file = open("input_large.in", "r")
output_file = open("output_large.txt", "w")

cases = int(input_file.readline())

for i in range(cases):

	s = list(input_file.readline())[0:-1]
	s = [ord(letter) for letter in s]

	output = []

	for letter in s:
		if not output:
			output.append(letter)
		else:
			if letter >= output[0]:
				output.insert(0,letter)
			else:
				output.append(letter)

	output = [chr(letter) for letter in output]
	output = "".join(output)
		
	output_file.write("Case #" + str(i+1) + ": " + output + "\n")