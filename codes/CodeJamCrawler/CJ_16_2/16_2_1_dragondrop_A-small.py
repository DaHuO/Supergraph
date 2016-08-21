#!/usr/bin/python
import sys
digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
digitl = []
for d in digits:
	digitl.append(list(d))

def getPhoneNumber( input ):
	input = list(input)
	last = 0
	output = []
	i = 0
	while "U" in input:
		output.append("4")
		for z in digitl[4]:
			if z not in input:
				print("ERROR:  " + str(input))
			input.remove(z)
	while "Z" in input:
		output.append("0")
		for z in digitl[0]:
			if z not in input:
				print("ERROR:  " + str(input))
			else:
				input.remove(z)
	while "X" in input:
		output.append("6")
		for z in digitl[6]:
			if z not in input:
				print("ERROR:  " + str(input))
			input.remove(z)
	while "G" in input:
		output.append("8")
		for z in digitl[8]:
			if z not in input:
				print("ERROR:  " + str(input))
			input.remove(z)
	while "W" in input:
		output.append("2")
		for z in digitl[2]:
			if z not in input:
				print("ERROR:  " + str(input))
			input.remove(z)
	while i < len(digitl):
		current = digitl[i]
		l = wordIn(input, current)
		if l != 0:
			input = l
			output.append(str(i))
		else:
			i += 1

	if (len(input) > 0):
		print("ERROR:  " + str(input))
	output.sort()
	return ''.join(output)

def wordIn(input, current):
	temp = list(input)
	for x in current:
		if x in temp:
			temp.remove(x)
		else:
			return 0
	return temp

def main( argv ):
	infile = open(argv[1], 'r');
	outfile = open('output.txt', 'w');
	cases = int(infile.readline())
	for case in range(1, cases+1):
		phoneNumber = getPhoneNumber(infile.readline().rstrip())
		print("Case #" + str(case) + ": " + str(phoneNumber), file=outfile)

if __name__ == "__main__":
    main(sys.argv)