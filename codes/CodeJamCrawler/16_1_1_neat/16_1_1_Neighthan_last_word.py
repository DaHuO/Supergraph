#!/usr/bin/python
import sys

def main(size):
	"""
	@param size = string; small or large
	"""
	infile = size + "_a.in"

	output = ""

	with open(infile) as file:
		num_cases = int(file.readline())
		for case in range(1, num_cases+1):
			last_word = find_last_word(file.readline())
			output += "Case #%s: %s\n" % (case, last_word)

	with open(size + "_a.out", 'w') as outfile:
		outfile.write(output)


def find_last_word(seq):
    last_word = seq[0]
    for i in range(1,len(seq)):
        if last_word[0] <= seq[i]:  # seq[i] comes later in alphabet
            last_word = seq[i] + last_word
        else:
            last_word += seq[i]
    return last_word

if __name__ == "__main__":
	main(sys.argv[1])


