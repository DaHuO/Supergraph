from string import ascii_uppercase
# "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
# Z: zero "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
# W: two "ONE", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
# X: six "ONE", "THREE", "FOUR", "FIVE", "SEVEN", "EIGHT", "NINE"
# U: four "ONE", "THREE", "FIVE", "SEVEN", "EIGHT", "NINE"
# O: one "THREE", "FIVE", "SEVEN", "EIGHT", "NINE"
# R: three  "FIVE", "SEVEN", "EIGHT", "NINE"
# G: eight "FIVE", "SEVEN", "NINE"
# S: seven "FIVE", NINE
# V: five NINE

T = int(raw_input())
for i in xrange(1,T+1):
	lettercount = {}
	for letter in ascii_uppercase:
		lettercount[letter] = 0

	word = raw_input()
	for letter in word:
		lettercount[letter] += 1

	number = []

	while lettercount['Z'] > 0:
		for letter in 'ZERO':
			lettercount[letter] -= 1
		number.append(0)
	while lettercount['W'] > 0:
		for letter in 'TWO':
			lettercount[letter] -= 1
		number.append(2)
	while lettercount['X'] > 0:
		for letter in 'SIX':
			lettercount[letter] -= 1
		number.append(6)
	while lettercount['U'] > 0:
		for letter in 'FOUR':
			lettercount[letter] -= 1
		number.append(4)
	while lettercount['O'] > 0:
		for letter in 'ONE':
			lettercount[letter] -= 1
		number.append(1)
	while lettercount['R'] > 0:
		for letter in 'THREE':
			lettercount[letter] -= 1
		number.append(3)
	while lettercount['G'] > 0:
		for letter in 'EIGHT':
			lettercount[letter] -= 1
		number.append(8)
	while lettercount['S'] > 0:
		for letter in 'SEVEN':
			lettercount[letter] -= 1
		number.append(7)
	while lettercount['V'] > 0:
		for letter in 'FIVE':
			lettercount[letter] -= 1
		number.append(5)
	while lettercount['N'] > 0:
		for letter in 'NINE':
			lettercount[letter] -= 1
		number.append(9)

	number.sort()
	result = ""
	for digit in number:
		result += str(digit)

	print "Case #"+str(i)+ ": " + result
