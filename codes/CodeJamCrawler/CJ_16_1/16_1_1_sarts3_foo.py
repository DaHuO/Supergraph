def last_word(word):
	new_word = ''
	for letter in word:
		begin = letter + new_word
		end = new_word + letter
		if begin > end:
			new_word = letter + new_word
		else:
			new_word += letter

	return new_word


def handle_input():
	i = 1
	first_line = raw_input()
	while i <= 100:
		print "Case #{}: {}".format(i, last_word(str(raw_input())))
		i += 1


if __name__ == "__main__":
    handle_input()