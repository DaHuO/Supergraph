T = raw_input()
T = int(T)

for i in range(T):

	N = raw_input()
	N = int(N)
	
	if N == 0:
		writeStr = "Case #"+str(i+1)+": INSOMNIA"
		print writeStr
		continue

	newN = N
	seenList = []
	multiplier = 0
	
	while len(seenList) != 10:
		multiplier = multiplier + 1
		newN = multiplier * N
		while newN > 0:
			num = newN % 10
			if num not in seenList:
				seenList.append(num)
			newN = newN / 10

	lastNumber = multiplier * N
	writeStr = "Case #"+str(i+1)+": "+str(lastNumber)
	print writeStr
