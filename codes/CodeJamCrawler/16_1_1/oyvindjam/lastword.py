
import sys

sys.stdin.readline()

f = open("output", "w")

for case, line in enumerate(sys.stdin, 1):
	letters = list(line.strip())

	word = letters[0]
	for letter in letters[1:]:
		if letter >= word[0]:
			word = letter + word
		else:
			word = word + letter
	

	f.write("Case #%d: %s\n" % (case, word))

f.close()

