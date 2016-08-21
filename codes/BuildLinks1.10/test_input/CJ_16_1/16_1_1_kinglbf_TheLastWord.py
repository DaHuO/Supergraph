'''
The Last Word:

Goal is to print the lexographically last possible "word" given the input.__base__
'''

f = open("C:\Projects\CodeJam2016-1A\TLW\A-large.in", "r+")
foutput = open("C:\Projects\CodeJam2016-1A\TLW\A-large.out","w+");
data = []
for line in f:
	data.append(line.strip())
        
for i in range(int(data[0])):
	letters = list(data[1+i])
	final_string = letters[0]
	for j in range(len(letters) - 1):
		if (final_string[0] <= letters[j + 1]):
			final_string = letters[j+1] + final_string
		else:
			final_string = final_string + letters[j+1]
	foutput.write("Case #" + str(i+1) + ": " + final_string + "\n")
	
foutput.close()