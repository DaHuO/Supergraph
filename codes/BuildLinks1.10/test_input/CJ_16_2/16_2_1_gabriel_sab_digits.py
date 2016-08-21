output = open('output_large.txt', 'w')

with open('input_large.txt', 'r') as file:
	numberOfCases = int(file.readline())
	for i in range(numberOfCases):
		result = []
		output.write("Case #" + str(i + 1) + ": ")
		letters = list(file.readline())
		while 'Z' in letters:
			for letter in list("ZERO"):
				letters.remove(letter)
			result.append('0')
		while 'W' in letters:
			for letter in list("TWO"):
				letters.remove(letter)
			result.append('2')
		while 'X' in letters:
			for letter in list("SIX"):
				letters.remove(letter)
			result.append('6')
		while 'G' in letters:
			for letter in list("EIGHT"):
				letters.remove(letter)
			result.append('8')
		while 'H' in letters:
			for letter in list("THREE"):
				letters.remove(letter)
			result.append('3')
		while 'R' in letters:
			for letter in list("FOUR"):
				letters.remove(letter)
			result.append('4')
		while 'O' in letters:
			for letter in list("ONE"):
				letters.remove(letter)
			result.append('1')
		while 'F' in letters:
			for letter in list("FIVE"):
				letters.remove(letter)
			result.append('5')
		while 'S' in letters:
			for letter in list("SEVEN"):
				letters.remove(letter)
			result.append('7')
		if (len(letters) > 1):
			for i in range((len(letters)-1)/4):
				result.append('9')
		result.sort()
		output.write("".join(result) + "\n")
output.close()