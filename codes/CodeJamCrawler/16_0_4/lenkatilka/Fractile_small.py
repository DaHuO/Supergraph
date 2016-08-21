
def main():

	import sys
	filename = sys.argv[1]

	with open(filename) as f:
		content = f.readlines()
	outputFile = open("outputSmallFractile.out", 'w')
	

	T = int(content[0])

	for test in range(T):

		index = 1 + test
		K, C, S = content[index].split()

		K, C, S = int(K), int(C), int(S)

		
		outputStr = "Case #" + str(test+1) + ": "

		checks = " ".join(str(ind) for ind in range(1, K + 1))
		outputStr += checks
		outputStr += "\n"

		outputFile.write(outputStr)

if __name__ == '__main__':
	main()
