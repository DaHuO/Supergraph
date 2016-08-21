for i in range(int(input())):
	facing = input()
	possibility = 1
	otherPossibility = 0
	flipCount = 0
	for index in range(len(facing)):
		if facing[index] == "+":
			possibility = 0
			otherPossibility = 0
		if facing[index] == "-":
			if possibility:
				if not otherPossibility:
					flipCount+=1
					otherPossibility = 1
			if not possibility:
				if not otherPossibility:
					flipCount +=2
					otherPossibility = 1
	print("Case #" + str(i+1) +": " + str(flipCount))