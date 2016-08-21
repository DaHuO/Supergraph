def showLastWord(input):
	i_list = list(input)
	result = ""
	for ktk in i_list:
		if result == "":
			result = ktk
		else:
			if result[0] > ktk:
				result = result + ktk
			else:
				result = ktk + result
	return result

input = int(raw_input())

for case in range(1, input+1):
	line = raw_input()
	print "Case #" + str(case) + ": " + showLastWord(line)