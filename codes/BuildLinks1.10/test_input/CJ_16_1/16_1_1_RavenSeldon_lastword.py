def get_final_word(letters):
	word = letters[0]
	if len(letters) == 1:
		return word

	for letter in letters[1:]:
		if letter >= word[0]:
			word = letter + word
		else:
			word = word + letter
	return word

# Test input/output
num_cases = int(raw_input())

for i in xrange(num_cases):
	letters = raw_input()
	lastword = get_final_word(letters)
	print("Case #" + str(i + 1) + ": " + lastword)