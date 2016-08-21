
def main():

	import sys
	filename = sys.argv[1]

	with open(filename) as f:
		content = f.readlines()
	outputFile = open("outputDigitsFile.out", 'w')
	

	T = int(content[0])

	for test in range(T):

		index = 1 + test

		numbers = findNumbers(content[index])
		numbers.sort()
		numbOutput = "".join(str(number) for number in numbers)

		outputStr = "Case #" + str(test+1) + ": "

		outputStr += numbOutput
		outputStr += "\n"

		outputFile.write(outputStr)

def findNumbers(mixed):
 
	chDict = {}
	numbers = []	

	for ch in mixed:
		if ch in chDict :
			chDict[ch] += 1
		else: 
			chDict[ch] = 1
	Uni = {0: "ZERO", 2: "WTO", 6: "XIS", 8: "GHTEI"}
	chDict, numbers = findUniDigits(chDict, Uni, numbers)

	Uni = {3: "HREET", 7: "SEVEN"}
	chDict, numbers = findUniDigits(chDict, Uni, numbers)
	Uni = {4: "RFOU"}
	chDict, numbers = findUniDigits(chDict, Uni, numbers)
	Uni = {5: "FIVE", 1: "ONE"}
	chDict, numbers = findUniDigits(chDict, Uni, numbers)
	Uni = {9: "NINE"}
	chDict, numbers = findUniDigits(chDict, Uni, numbers)
	

			
	return(numbers)

def findUniDigits(chDict, Uni, numbers):
	for unique in Uni:
		while Uni[unique][0] in chDict :
			numbers.append(unique)
			for ch in Uni[unique]:
				chDict[ch] -= 1
				if chDict[ch] == 0:
					del chDict[ch]

	return(chDict, numbers)

if __name__ == '__main__':
	main()
