input_file = "input"
output_file = "output"

content = open(input_file).readlines()
cases = content[1:]

results = []
for case in cases:
	digits = set()
	if case == "0":
		results.append("INSOMNIA")
		break
	for i in range(1, 10000):
		current_case = str(int(case) * i)
		[digits.add(c) for c in current_case]
		if len(digits) == 10:
			results.append(current_case)
			break
	else:
		results.append("INSOMNIA")

output = open(output_file, "w+")
for i in range(len(cases)):
	output.write("Case #" + str(i+1) + ": " + results[i] + "\n")