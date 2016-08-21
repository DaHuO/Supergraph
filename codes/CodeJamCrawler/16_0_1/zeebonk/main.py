import fileinput
from collections import Counter


if __name__ == '__main__':
	lines = fileinput.input()
	next(lines)
	for case, line in enumerate(lines):
		number = int(line)
		multiplier = 1
		counts = {str(i):0 for i in xrange(10)}
		while not all(c > 0 for c in counts.itervalues()) and multiplier < 1000000:
			for c in str(number * multiplier):
				counts[c] += 1
			multiplier += 1
		if multiplier == 1000000:
			print "Case #%d: INSOMNIA" % (case + 1)
		else:
			print "Case #%d: %d" % (case + 1, number * (multiplier-1))
