import fileinput
from collections import Counter


level_1 = {
	'Z': ('ZERO', 0),
	'W': ('TWO', 2),
	'X': ('SIX', 6),
	'G': ('EIGHT', 8),
}

level_2 = {
	'H': ('THREE', 3),
	'U': ('FOUR', 4),
	'S': ('SEVEN', 7),
}

level_3 = {
	'F': ('FIVE', 5),
	'O': ('ONE', 1),
}

level_4 = {
	'N': ('NINE', 9),
}


def main():
	stream = fileinput.input()
	next(stream)
	for case, line in enumerate(stream):
		number = []
		letter_counts = Counter(line.strip())

		ok = True
		while ok:
			ok = False
			for key, (chars, digit) in level_1.iteritems():
				if letter_counts[key] > 0:
					ok = True
					number.append(digit)
					letter_counts.subtract(chars)

		ok = True
		while ok:
			ok = False
			for key, (chars, digit) in level_2.iteritems():
				if letter_counts[key] > 0:
					ok = True
					number.append(digit)
					letter_counts.subtract(chars)

		ok = True
		while ok:
			ok = False
			for key, (chars, digit) in level_3.iteritems():
				if letter_counts[key] > 0:
					ok = True
					number.append(digit)
					letter_counts.subtract(chars)

		ok = True
		while ok:
			ok = False
			for key, (chars, digit) in level_4.iteritems():
				if letter_counts[key] > 0:
					ok = True
					number.append(digit)
					letter_counts.subtract(chars)

		print "Case #%d: %s" % (case + 1, ''.join(map(str, sorted(number))))


if __name__ == '__main__':
	main()
