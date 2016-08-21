# /usr/bin/env python3

def combos(s):
	digits = list(s)
	unknowns = digits.count('?')
	for i in range(10 ** unknowns):
		yield translate(digits, i)

def translate(digits, n):
	digits = list(digits)
	unknowns = 0
	for i in range(len(digits)):
		if (digits[i] == '?'):
			digits[i] = str((n // (10 ** unknowns)) % 10)
			unknowns += 1
	s = ''.join(digits)
	return int(s)

T = int(input())
for case_number in range(T):
	case_string = "Case #" + str(case_number + 1) + ":"
	s = input().split()
	C = s[0]
	J = s[1]

	best_d = 999999999999999999999999999
	best_pair = None
	for c in combos(C):
		for j in combos(J):
			d = abs(c - j)
			if d < best_d:
				best_d = d
				best_pair = (c, j)
			elif d == best_d:
				if c < best_pair[0] or j < best_pair[1]:
					best_pair = (c, j)


	print(case_string, str(best_pair[0]).zfill(len(C)), str(best_pair[1]).zfill(len(J)))
