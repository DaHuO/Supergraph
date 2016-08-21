DIGITS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"];

def solve(input):
	chars = {}
	for c in input:
		if chars.has_key(c):
			chars[c] = chars[c] + 1
		else:
			chars[c] = 1
	digits = solveHelper(chars, [])
	return ''.join(str(x) for x in digits)

def solveHelper(chars, digits):
	curDigits = digits[:]
	if isEmpty(chars):
		return curDigits
	for index in range(len(DIGITS)):
		d = DIGITS[index]
		if containsDigit(chars, d):
			for x in d:
				chars[x] = chars[x] - 1
			curDigits.append(index)
			sol = solveHelper(chars, curDigits)
			if sol is None:
				for x in d:
					chars[x] = chars[x] + 1
				curDigits = digits[:]
			else:
				return sol
	return None

def isEmpty(chars):
	for c in chars:
		if chars[c] > 0:
			return False
	return True

def containsDigit(chars, d):
	digitsChars = {}
	for c in d:
		if digitsChars.has_key(c):
			digitsChars[c] = digitsChars[c] + 1
		else:
			digitsChars[c] = 1
	for x in digitsChars:
		if not chars.has_key(x) or chars[x] < digitsChars[x]:
			return False
	return True


f = open('A-small-attempt2.in', 'r')
lines = f.read().split('\n')
numCases = int(lines[0])
cases = lines[1:]
for i in range(numCases):
	print 'Case #' + str(i + 1) + ': ' + solve(cases[i])