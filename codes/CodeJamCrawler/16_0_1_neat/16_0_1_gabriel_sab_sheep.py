output = open('output_large.txt', 'w')

with open('input_large.txt', 'r') as f:
	numberOfCases = f.readline()
	for i in range(int(numberOfCases)):
		number = int(f.readline())
		if number == 0:
			output.write("Case #" + str(i+1) + ": INSOMNIA\n")
		else:
			seen = []
			round = 1
			last = number
			while len(seen) < 10:
				n = round*number
				last = n
				for c in str(n):
					if c not in seen:
						seen.append(c)
				round += 1
			output.write("Case #" + str(i+1) + ": " + str(last))
			if i < int(numberOfCases) -1:
				output.write("\n")