import sys

INPUT_FILE_NAME = sys.argv[-1]

input_file = open(INPUT_FILE_NAME, 'r')
output_file = open('output.txt', 'w')

numLines = int(input_file.readline())


for x in xrange(0,numLines):
	seen = {
		"0":0,
		"1":0,
		"2":0,
		"3":0,
		"4":0,
		"5":0,
		"6":0,
		"7":0,
		"8":0,
		"9":0
	}

	ostr = "Case #%d: " % (x+1) 
	inputStr = int(input_file.readline().split()[::-1][0])

	lastSeen = "INSOMNIA"

	if inputStr == 0:
		pass

	else:
		x = 0

		while 0 in seen.values():
			x+=1
			lastSeen = inputStr * x
			
			digits = list(str(lastSeen))

			for eachDig in digits:
				seen[eachDig] = 1

	ostr += str(lastSeen)	

	output_file.write(ostr.strip())
	output_file.write("\n")
		

