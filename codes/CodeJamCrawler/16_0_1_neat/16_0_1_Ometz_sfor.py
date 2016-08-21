
import sets

def sfor(num):
	digits, i = sets.Set([]), 1
	if num == 0:
		return 'INSOMNIA'
	
	while len(digits) != 10:
		for j in str(num*i):
			digits.add(j)
		i += 1

	return str(num*(i-1))
	
	
def main():
	file = open('input.txt', 'r')
	testCases, cases = int(file.readline()), file.readlines()
	file.close()
	
	file = open('output.txt', 'w')
	for line in range(testCases):
		file.write('Case #' + str(line+1) + ': ' + sfor(int(cases[line])) + '\n')
	
	file.close()
	
main()