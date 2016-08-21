def solve(inputs):

	d = {"Z": "ZERO", "W": "TWO", "U": "FOUR", "X": "SIX", "G": "EIGHT"}
	d2 = {"F": "FIVE", "O": "ONE", "H": "THREE"}
	d3 = {"V": "SEVEN", "I": "NINE"}

	mapping = {"ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}

	input_d = dict()
	result = dict()

	for i in inputs:
		if i in input_d:
			input_d[i] += 1
		else:
			input_d[i] = 1

	print(input_d)
	print(inputs)

	for i in inputs:
		if input_d[i] > 0 and i in d:
			word = d[i]

			for w in word:
				input_d[w] -= 1

			if word in result:
				result[word] += 1
			else:
				result[word] = 1

	for i in inputs:
		if input_d[i] > 0 and i in d2:
			word = d2[i]

			for w in word:
				input_d[w] -= 1

			if word in result:
				result[word] += 1
			else:
				result[word] = 1

	for i in inputs:
		if input_d[i] > 0 and i in d3:
			word = d3[i]

			for w in word:
				input_d[w] -= 1

			if word in result:
				result[word] += 1
			else:
				result[word] = 1

	output = [0 for i in range(10)]
	for r in result:
		output[mapping[r]] += result[r]

	o = ""
	for i in range(10):
		if output[i] != 0:
			o += str(i) * output[i]

	print(o)
	return o


input_file_name = "A-large.in"
output_file_name = "output.out"


with open(input_file_name, "r") as input:
	number_cases = int(input.readline())

	with open(output_file_name, "w") as output:

		for i in range(number_cases):

			inputs = input.readline().strip()

			result = solve(inputs)

			if result is None:
				print("NOOOOOOOO")
			elif result ==  "IMPOSSIBLE":
				output.write("Case #" + str(i + 1) + ": " + result + "\n")
			else:
				output.write("Case #" + str(i + 1) + ": " + result + "\n")

