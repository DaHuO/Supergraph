num_cases = int(input())

for i in range(num_cases):
	line = input()
	result = 0
	if line[0] == "-":
		result += 1
	for j in range(1, len(line)):
		if line[j] == line[j-1]:
			pass
		elif line[j] == "-":
			result += 2
		elif line[j] == "+":
			pass
	print("Case #" + str(i+1) + ": " + str(result))


