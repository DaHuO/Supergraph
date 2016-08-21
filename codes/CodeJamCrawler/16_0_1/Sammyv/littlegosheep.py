def littlegosheep():

	f = open('A-large.txt', 'r')
	lines = f.readlines()
	t = int(lines[0])

	for repeats in range (1,t + 1):
		Countten = [0] *10
		N = int(lines[repeats])
		notallten = True
		i = 1
		
		if N != 0:
			while (notallten):
				currentN = N * i
				i += 1
				tempN = currentN
			
				while (tempN >= 1):
					digit = tempN % 10
					Countten[digit] = 1
					tempN = tempN /10
			
			
				if 0 not in Countten:
					notallten = False
		
			print ("Case #" + str(repeats) + ": " + str(currentN))
			
		else:
			print ("Case #" + str(repeats) + ": INSOMNIA")
			
littlegosheep()