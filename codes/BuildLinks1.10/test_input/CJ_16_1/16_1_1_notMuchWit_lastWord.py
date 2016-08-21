def getLastWord():
	with open("A-large.in.txt") as f:
		numOfCases = int(f.readline())
		for case in range(numOfCases):
			lastWord = []
			firstLetter = ""
			for letter in f.readline():
				if firstLetter == "":
					firstLetter = letter

				# If the letter is alphabetically larger than the first, put it at the front. Otherwise, back.
				if ord(letter) >= ord(firstLetter):
					lastWord.insert(0, letter)
					firstLetter = letter
				else:
					lastWord.append(letter)

			# Print the last word we found.
			print("Case #" + str(case + 1) + ": " + "".join(lastWord).strip())


getLastWord()