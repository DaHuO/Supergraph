# Tony E
# Counting Sheep

OutputStr = "Case #%d: %s"

def CountSheep(CaseNumber, Number):
	"""Takes an input N and prints 'Case #X: Y'"""
	if (Number == 0):
		print(OutputStr % (CaseNumber, "INSOMNIA"))
	else:

		#Empty structure to keep track of which numbers have been seen
		#Map to avoid converting back to int in a python list
		DigitMap = dict()
		CurrentNumber = 0

		while (len(DigitMap) < 10):
			CurrentNumber += Number
			for i in str(CurrentNumber):
				DigitMap[i] = None

		print(OutputStr % (CaseNumber, CurrentNumber))
		

def main(Text):
	"""Takes main function and runs with it"""
	N = int(Text[0])

	for i in range(1, N + 1):
		CountSheep(i, int(Text[i]))



if __name__ == "__main__":
	import sys
	#Extract the info
	File = open(sys.argv[1])
	Text = File.readlines()
	File.close()

	main(Text)