
def main():

	import sys
	filename = sys.argv[1]

	with open(filename) as f:
		content = f.readlines()
	outputFile = open("outputPancakes.out", 'w')
	

	T = int(content[0])

	for test in range(T):

		index = 1 + test
		pancakes = content[index]
		if pancakes == '': flips = 0
		else: flips = countFlips(pancakes)
		
		outputStr = "Case #" + str(test+1) + ": "

		result = str(flips)
		outputStr += result
		outputStr += "\n"

		outputFile.write(outputStr)

def countFlips(pancakes):

	firstCh = pancakes[0]
	lenPancakes = len(pancakes)
	previous = firstCh
	patches = 1

	for ind in range(1,lenPancakes):
		if (pancakes[ind] != previous) and (pancakes[ind] != "\n"):
			patches += 1
		previous = pancakes[ind]	

	if firstCh == '-':
		if patches % 2 == 0: return(patches-1)
		else: return(patches)

	else:
		if patches % 2 == 0: return(patches)
		else: return(patches-1)

if __name__ == '__main__':
	main()
