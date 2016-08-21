

def main():
	inputFile = open('D-small-attempt0.in', 'r')
	outputFile = open('fracOutput.txt', 'w')
	cases = int(inputFile.readline().strip())
	for i in xrange(cases):
		K, C, S = [int(x) for x in inputFile.readline().strip().split()]
		outputFile.write('Case #' + str(i + 1) + ': ')
		if S < K:
			outputFile.write('IMPOSSIBLE\n')
		else:
			for i in range(S):
				outputFile.write(str(i + 1) + ' ')
			outputFile.write('\n')

main()