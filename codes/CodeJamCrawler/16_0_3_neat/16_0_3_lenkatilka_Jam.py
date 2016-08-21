
def main():

	import sys
	filename = sys.argv[1]

	with open(filename) as f:
		content = f.readlines()
	outputFile = open("outputJamFile.out", 'w')
	

	T = int(content[0])

	for test in range(T):

		index = 1 + test
		N, J = content[index].split()
		N, J = int(N), int(J)
		print(N,J)

		newDigits = int(N/2) - 1

		outputCase = "Case #" + str(test+1) + ":\n"
		outputFile.write(outputCase)

		## each number N in base k is divisible by a number k+1
		## if the number in base k has the same number of "1" on
		## even and odd positions. this is because ( k^p % (k+1) ) == 1
		## if p is odd and (k^p % k) == -1 if p is even. then if
		## we have x times 1 on odd places and x times -1 on even places,
		## the total remainder of N % (k+1) == 0

		## numbers that have the same number of ones on odd and even places are
		## constructed such that we find distinct numbers composed of 8 digits 
		## that are 0 or one and add another 8 digits that are a rotation of
		## first 8 digits by 180 degrees:
		for number in range(1,J+1):
			print(number)
			firstHalf = "1"+bin(number)[2::].zfill(newDigits)
			print(firstHalf)
			validSolution = firstHalf + firstHalf[-1::-1]	

			dividers = " ".join(str(divider) for divider in range(3,12))
			outputStr = validSolution + " " + dividers
			outputStr += "\n"

			outputFile.write(outputStr)

if __name__ == '__main__':
	main()
