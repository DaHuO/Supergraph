def getNumOfFlips():
	with open("B-large.in.txt") as f:
		numOfTest = int(f.readline())
		for test in range(numOfTest):
			cakeStacks = f.readline().split()
			numOfFlips = 0
			executerIndex = 0
			flipExecuter = ["-", "+"]
			for cakes in cakeStacks:
				for cake in cakes[::-1]:
					if(cake == flipExecuter[executerIndex % len(flipExecuter)]):
						numOfFlips += 1
						executerIndex += 1

			print("Case #" + str(test + 1) + ": " + str(numOfFlips))

getNumOfFlips()