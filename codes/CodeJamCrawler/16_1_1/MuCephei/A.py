def WinningWord(inputString):
	result = ""
	for letter in inputString:
		if not result or result[0] > letter:
			result = result + letter
		else:
			result = letter + result

	return result


times = input()

for x in range(times):
    print ("Case #" + str(x+1) + ": " + WinningWord(str(raw_input())))