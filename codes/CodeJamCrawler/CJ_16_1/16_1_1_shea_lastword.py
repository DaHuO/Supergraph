# from test import test


def thelastword(s):

	word = s[0]
	s = s[1:]

	for l in s:
		word1 = l + word
		word2 = word + l
		word = sorted([word1, word2])[-1]

	return word


def test(func, filename):
	input_file = open('tests/' + filename + '.in')
	output_file = open('tests/' + filename + '.out', 'w')
	lines = input_file.readlines()

	cases = int(lines[0])
	for case in range(1, cases + 1):
		line = lines[case].strip()
		result = func(line)
		print('Case #{}: {}'.format(case, result), file=output_file)


if '__main__' == __name__:
	test(thelastword, 'A-large')
