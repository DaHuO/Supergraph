with open ('A-large.in') as file:
	numberOfTasks = file.readline()
	input = file.readlines()

result = {}

with open ('largeA.output', 'w') as output:
	case = 1
	for line in input:
		initialValue = line
		digits = set ()
		value = int(initialValue)
		if value == 0:
			output.write("Case #" + str(case)+ ": " + "INSOMNIA\n")
		else:
			for digit in initialValue:
				digits.add(digit)
			multiplier = 2
			while len(digits) <= 10:
				newNumber = multiplier*value
				newValue = str(newNumber)
				for digit in newValue:
					digits.add(digit)
				multiplier += 1
			output.write("Case #" + str(case)+ ": " + str(newNumber) + "\n")
		case += 1
