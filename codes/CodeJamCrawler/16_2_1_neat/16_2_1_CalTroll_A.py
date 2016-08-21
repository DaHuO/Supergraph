mapping = {
	0: ('ZERO', 'Z'),
	1: ('ONE', 'O'),
	2: ('TWO', 'W'),
	3: ('THREE', 'T'),
	4: ('FOUR', 'U'),
	5: ('FIVE', 'F'),
	6: ('SIX', 'X'),
	7: ('SEVEN', 'S'),
	8: ('EIGHT', 'I'),
	9: ('NINE', 'N'),
}

order = [0, 2, 6, 4, 5, 1, 7, 9, 8, 3]

mem = {}
def solve(S_dict):
	outarr = []
	for i in order:
		string, letter = mapping[i]
		while (letter in S_dict and S_dict[letter] > 0):
			for c in string:
				S_dict[c] -= 1
			outarr.append(i)
	return ''.join([str(el) for el in sorted(outarr)])





T = input()
for i in range(T):
	S = raw_input()
	S_dict = {}
	for c in S:
		if c not in S_dict:
			S_dict[c] = 0
		S_dict[c] += 1
	sol = solve(S_dict)
	print 'Case #' + str(i + 1) + ': ' + sol

