from sys import *


fin = open(argv[1] + ".in", 'r') 
fout = open(argv[1] + ".out", 'w')

numbers = [
		('Z', "ZERO", 0),
		('X', "SIX", 6),
		('S', "SEVEN", 7),
		('V', "FIVE", 5),
		('G', "EIGHT", 8),
		('W', "TWO", 2),
		('H', "THREE", 3), 
		('F', "FOUR", 4),
		('I', "NINE", 9),
		('O', "ONE", 1)
]

def calc_number(word):
	word = word[:-1]
	digits = [ 0 for i in range(0, 10) ]
	letters = {}
	for letter in word:
		if letter in letters:
			letters[letter] = letters[letter] + 1
		else:
			letters[letter] = 1
	
	for num in numbers:
		if not num[0] in letters or letters[num[0]] == 0:
			continue
		count = letters[num[0]]
		digits[num[2]] = count
		for c in num[1]:
			letters[c] = letters[c] - count
	result = ""
	for digit in range(0, 10):
		for i in range(0, digits[digit]):
			result = result + str(digit)
	return result

	

ncases = int(fin.readline())
for c in range(0, ncases):
	fout.write("Case #" + str(c+1) + ": " + calc_number(fin.readline()) + "\n")

fin.close()
fout.close()


	
