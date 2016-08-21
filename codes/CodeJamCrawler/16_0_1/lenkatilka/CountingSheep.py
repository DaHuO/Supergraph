
def main():

	import sys
	filename = sys.argv[1]

	with open(filename) as f:
		content = f.readlines()
	outputFile = open("outputSheepFile.out", 'w')
	

	T = int(content[0])

	for test in range(T):

		index = 1 + test
		num = int(content[index])

		result = findLatest(num)		

		outputStr = "Case #" + str(test+1) + ": "

		lastNum = str(result)
		outputStr += lastNum
		outputStr += "\n"

		outputFile.write(outputStr)

def findLatest(num):
	if num == 0: return("INSOMNIA")
	from collections import defaultdict

	digits = []
	k = 1

	while True:	
		check = k*num	
		while check > 0:
			digit = check % 10
			if digit not in digits:
				digits.append(digit)
				if len(digits) == 10: return(k*num)

			check = int(check/10)

		k += 1

if __name__ == '__main__':
        main()

