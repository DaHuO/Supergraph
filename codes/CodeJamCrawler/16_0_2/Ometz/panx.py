
from ran import ran

def panx(string):
	flips, string = 0, list(string)
	
	if len(string) == 1:
		return 1 if string == ['-'] else 0
		
	while string != list('+'*len(string)):
		for char in ran(string[:-1]):
			if string[char]+string[char+1] == '-+':
				flips += 1
				for index in ran(char+1):
					string[index] = '+' if string[index] == '-' else '-'
			elif string[-1] == '-':
				flips += 1
				for char in ran(string):
					string[char] = '+' if string[char] == '-' else '-'
	
	return flips
	
def main():
	file = open('input.txt', 'r')
	testCases, cases = int(file.readline()), file.readlines()
	file.close()
	
	file = open('output.txt', 'w')
	for index in ran(testCases):
		file.write('Case #' + str(index+1) + ': ' + str(panx(cases[index][:-1])) + '\n')
	file.close()
	
main()

