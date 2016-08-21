output = open('output_large.txt', 'w')

def solve(pile):
	if True not in pile:
		return 1
	else:
		count = 0
		while False in pile:
			if True not in pile:
				return count + 1
			first = pile[0]
			for j in range(1, len(pile)):
				if not pile[j] == first:
					count += 1
					pile = [not e for e in list(reversed(pile[:j]))] + pile[j:]
					break
		return count

with open('input_large.txt', 'r') as file:
	numberOfCases = int(file.readline())
	for i in range(numberOfCases):
		line = file.readline()
		pile = []
		for c in line:
			if c == '-':
				pile.append(False)
			else:
				pile.append(True)
		count = solve(pile)
		output.write("Case #" + str(i + 1) + ": " + str(count))
		if (i < numberOfCases - 1):
			output.write("\n")