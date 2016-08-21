#!/usr/bin/python

print ("hello Ahmad")


infile = open("A-large.in", "r")
outfile = open("output.in", "w")

testCases = infile.readline()

# num = input("Enter the number: ")

for i in range(0, int(testCases)):
	numsSeen = [False] * 10
	num = int(infile.readline())
	if (num == 0):
		outfile.write("Case #%s: INSOMNIA\n" % (i+1))
	else:
		count = 0
		currNum = num
		while not (all(numsSeen)):
			for letter in (str(currNum)):
				numsSeen[int(letter)] = True

			count = count + 1
			currNum = count*num
			
		outfile.write("Case #%s: %s\n" % (i+1, currNum-num))	
