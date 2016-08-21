#Google Code Jam - Qualification Round 2016

inputfile = open('A-large.in')
outputfile = open('output.txt', 'w')
caseNum = 1

numCases = int(inputfile.readline())

def findLast( number_string ):
	n = int(number_string)
	if (n == 0):
		return 'INSOMNIA'

	i = 1
	last_number = n
	digits = set(list('0123456789'))
	digits = digits - set(list(str(n)))

	while( len(digits) > 0 ):
		i += 1
		last_number = n * i
		digits = digits - set(list(str(last_number)))

	return str(last_number)

# Read each number and determine the last number
for line in inputfile:
	outputfile.write('Case #' + str(caseNum) + ': ' + findLast(line.strip()) + '\n')
	caseNum += 1