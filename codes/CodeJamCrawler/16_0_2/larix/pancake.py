import re

with open ('B-large.in') as file:
	numberOfTasks = file.readline()
	input = file.readlines()

with open ('Blarge.output', 'w') as output:
	case =1 
	for line in input:
		groups = 1
		for i in range(len(line)-1):
			# print i
			current = line[i]
			if (i+1) < len(line)-1:
				next = line[i+1]
				if current !=next:
					groups +=1
		if line[len(line)-2] == "+":
			groups -= 1
		output.write("Case #" + str(case)+ ": " + str(groups) + "\n")
		case += 1

