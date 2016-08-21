output = open('output.txt', 'w')

with open('input.txt', 'r') as file:
	numberOfCases = int(file.readline())
	for i in range(numberOfCases):
		output.write("Case #" + str(i + 1) + ": ")
		params = file.readline().split(" ")
		k = int(params[0])
		c = int(params[1])
		s = int(params[2])
		if k == s:
			for j in range(k):
				output.write(str(j + 1))
				if j < k -1:
					output.write(" ")
		else:
			output.write("IMPOSSIBLE")
		if i < numberOfCases - 1:
				output.write("\n")
			
output.close()