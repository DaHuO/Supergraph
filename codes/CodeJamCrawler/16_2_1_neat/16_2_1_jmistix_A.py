#input_set = "A-small.in"
#input_set = "A-small-attempt0.in"
input_set = "A-large.in"
from string import ascii_uppercase

def ind_by_char(char):
	return ord(char) - ord('A')

def get_phone(word):
	letters = {}
	for char in ascii_uppercase:
		letters[char] = 0
	for char in word:
		letters[char] += 1

	numbers = [
		('Z', 'ZERO', 0),
		('W', 'TWO', 2),
		('U', 'FOUR', 4),
		('X', 'SIX', 6),
		('G', 'EIGHT', 8),
		('H', 'THREE', 3),
		('F', 'FIVE', 5),
		('V', 'SEVEN', 7),
		('I', 'NINE', 9),
		('O', 'ONE', 1)
	]
	result_number = []
	for uniq, number, digit in numbers:
		while letters[uniq] > 0:
			result_number.append(digit)
			for char in number:
				letters[char] -= 1
	
	for char, q in letters.iteritems():
		assert q == 0

	return "".join(str(x) for x in sorted(result_number) )


with open(input_set) as cases:
	case_number = 0
	next(cases)

	for data in cases:
		case_number += 1
		#print case_number
		word = data.strip()
		print "Case #{}: {}".format(case_number, get_phone(word))