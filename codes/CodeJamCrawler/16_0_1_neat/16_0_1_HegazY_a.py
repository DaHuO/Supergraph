def AddUnique(number, seen):
	for x in str(number):
		if (x) not in seen:
			seen.append(x)

	return seen

def getResults(number):
	seen = []
	seen = AddUnique(number, seen)
	print seen

	if len(seen) == 10:
		return number

	total = number
	while len(seen) != 10:
		total += number
		seen = AddUnique(total, seen)

	return total


with open("test.txt", "r") as ins:
	ins.readline()
	i = 1
	with open("results.txt", "w") as out:
		for line in ins:

			number = int(line)

			if (number == 0):
				result = 'INSOMNIA'
			else:
				result = getResults(number)


			out.write('Case #%d: %s\n' % (i, result))
			i+=1