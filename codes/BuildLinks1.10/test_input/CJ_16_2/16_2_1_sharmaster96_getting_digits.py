def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('A-large.in', 'r'), open('A-large.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	counts = {}
	S = in_file.readline()[:-1]
	for c in S:
		if c in counts:
			counts[c] += 1
		else:
			counts[c] = 1
	number = ''

	# Handle 0
	if 'Z' in counts:
		number += '0'*counts['Z']
		for k in ['E', 'R', 'O']:
			if k in counts:
				counts[k] -= counts['Z']
		counts['Z'] = 0

	# Handle 6
	if 'X' in counts:
		number += '6'*counts['X']
		for k in ['S', 'I']:
			if k in counts:
				counts[k] -= counts['X']
		counts['X'] = 0

	# Handle 2
	if 'W' in counts:
		number += '2'*counts['W']
		for k in ['T', 'O']:
			if k in counts:
				counts[k] -= counts['W']
		counts['W'] = 0

	# Handle 8
	if 'G' in counts:
		number += '8'*counts['G']
		for k in ['E', 'I', 'H', 'T']:
			if k in counts:
				counts[k] -= counts['G']
		counts['G'] = 0

	# Handle 3
	if 'H' in counts:
		number += '3'*counts['H']
		for k in ['T', 'R', 'E', 'E']:
			if k in counts:
				counts[k] -= counts['H']
		counts['H'] = 0

	# Handle 4
	if 'R' in counts:
		number += '4'*counts['R']
		for k in ['F', 'O', 'U']:
			if k in counts:
				counts[k] -= counts['R']
		counts['R'] = 0

	# Handle 5
	if 'F' in counts:
		number += '5'*counts['F']
		for k in ['I', 'V', 'E']:
			if k in counts:
				counts[k] -= counts['F']
		counts['F'] = 0

	# Handle 1
	if 'O' in counts:
		number += '1'*counts['O']
		for k in ['N', 'E']:
			if k in counts:
				counts[k] -= counts['O']
		counts['O'] = 0

	# Handle 7
	if 'S' in counts:
		number += '7'*counts['S']
		for k in ['E', 'V', 'E', 'N']:
			if k in counts:
				counts[k] -= counts['S']
		counts['S'] = 0

	# Handle 9
	if 'I' in counts:
		number += '9'*counts['I']

	list_num = sorted([int(x) for x in number])
	epilogue("".join([str(x) for x in list_num]), case_num)


