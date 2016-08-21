from copy import copy

infile = open('A-small-attempt2.in', 'r')
outfile = open('test.out', 'w')

T = int(infile.readline())

Digits = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")

def works(digits, S, attempt):
	if len(S) == 0:
		return attempt
	for d in digits:
		tmp = copy(S)
		for i in range(len(d)):
			if d[i] in tmp:
				tmp.remove(d[i])
		if len(tmp) + len(d) == len(S):
			S = tmp
			attempt.append(d)
			return works(Digits, S, attempt)
	p = attempt.pop(-1)
	for l in p:
		S.append(l)
	return works(Digits[Digits.index(p)+1:], S, attempt)


def convert(digits, dlst):
	ans = ''
	for i in dlst:
		ans += str(digits.index(i))
	return ans

for t in range(1, T+1):
	word = infile.readline().strip()
	word = list(word)
	ans = convert(Digits, works(Digits, word, []))
	outfile.write('Case #' + str(t) + ': ' + ans + '\n')