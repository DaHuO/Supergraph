'''
Getting the Digits
'''

f = open(r"C:\Projects\CodeJam2016\1B\GtD\A-large.in", "r+")
foutput = open(r"C:\Projects\CodeJam2016\1B\GtD\A-large.out","w+")
data = []
for line in f:
	data.append(line.strip())

numbers = []
for i in range(int(data[0])):
	letters = list(data[1+i])
	numbers = [0,0,0,0,0,0,0,0,0,0]
	numbers[0] = letters.count("Z")
	numbers[2] = letters.count("W")
	numbers[4] = letters.count("U")
	numbers[6] = letters.count("X")
	numbers[8] = letters.count("G")
	
	numbers[1] = letters.count("O") - numbers[0] - numbers[2] - numbers[4]
	numbers[3] = letters.count("H") - numbers[8]
	numbers[5] = letters.count("F") - numbers[4]
	numbers[7] = letters.count("V") - numbers[5]
	
	numbers[9] = letters.count("I") - numbers[6] - numbers[5] - numbers[8]
	final_string = ""
	for j in range(10):
		final_string += numbers[j]*str(j)
		
	foutput.write("Case #" + str(i+1) + ": " + final_string + "\n")
	
foutput.close()