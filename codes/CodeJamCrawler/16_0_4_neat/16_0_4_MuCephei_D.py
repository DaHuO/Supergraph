def Cantor():
	parameters = raw_input()
	k = int(parameters.split()[0])
	c = int(parameters.split()[1])
	s = int(parameters.split()[2])
	scheduledCleaning = ""
	if (k / c) <= s:
		sectionsToCheck = range(k)
		currentCheck = 0
		while currentCheck < len(sectionsToCheck):
			spot = 1
			if currentCheck + c <= sectionsToCheck:
				toDo = sectionsToCheck[currentCheck:currentCheck + c]
				currentCheck += c
			else:
				toDo = sectionsToCheck
				currentCheck = len(sectionsToCheck)

			for depth in reversed(range(len(toDo))):
				spot = spot + (k**depth) * toDo[depth]
			scheduledCleaning = scheduledCleaning + " " + str(spot)
		return scheduledCleaning

	else:
		return "IMPOSSIBLE"

times = input()

for x in range(times):
    print ("Case #" + str(x+1) + ":" + str(Cantor()))