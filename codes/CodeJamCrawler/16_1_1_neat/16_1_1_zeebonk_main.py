import fileinput
from collections import Counter


if __name__ == '__main__':
	lines = fileinput.input()
	next(lines)
	for case, in_word in enumerate(lines, start=1):
		in_word = in_word.strip()
		last_words = [
			[in_word[0]]
		]
		for c in in_word[1:]:
			new_last_words = []
			for last_word in last_words:
				new_last_words.append([c] + last_word)
				new_last_words.append(last_word + [c])
			last_words = new_last_words
		print "Case #%d:" % case, ''.join(sorted(last_words)[-1])
