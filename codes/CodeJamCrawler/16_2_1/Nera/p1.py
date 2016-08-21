import sys

if len(sys.argv) != 3:
	print "Usage: problem1 <input file> <output file>"
	exit();

cases = []
inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()
for i in range(1, len(lines)):
	cases += [lines[i].strip()]

WORDS = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}

ORDERED_WORDS = ["TWO", "SIX", "ZERO", "SEVEN", "FIVE", "FOUR", "ONE", "THREE", "NINE", "EIGHT"]



def canFormNumber(chars, number):
	res = True
	for c in number:
		if c not in chars or chars[c] <= 0:
			res = False
	return res

def decrement(chars, number):
	for c in number:
		chars[c] = chars[c] - 1
	return chars

output = open(sys.argv[2], "w")

for case in range(0, len(cases)):
	string = cases[case]
	char_counts = {}
	for i in range(0, len(string)):
		c = string[i]
		if c not in char_counts:
			char_counts[c] = 0
		char_counts[c] = char_counts[c] + 1
	found_numbers = []
	#import pdb; pdb.set_trace()
	for number in ORDERED_WORDS:
		while canFormNumber(char_counts, number):
			found_numbers += [WORDS[number]]
			char_counts = decrement(char_counts, number)
	for c in char_counts:
		if char_counts[c] != 0:
			print "ERROR: " + string
	# print sorted(found_numbers)
	found_numbers = sorted(found_numbers)
	phone = ""
	for num in found_numbers:
		phone += str(num)
	output.write("Case #%d: %s\n" % (case + 1, phone))
output.close()