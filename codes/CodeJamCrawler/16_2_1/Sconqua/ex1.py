# Number of test cases
n = int(raw_input())
#print "NUMERO CASI %d " % n

for test in xrange(1, n+1):
	s = raw_input()
#	print "STRINGA : %s" % s
	dizionario = dict()
	result = list()

	allletters = "ZERONTWHFUIVSXG"
	for let in allletters:
		dizionario[let] = 0

	# conto il numero di ogni lettera e le regole le faccio da li,
	for lettera in s:
		dizionario[lettera.upper()] += 1

	# apply rules
	while dizionario['Z'] > 0:
		for let in "ZERO":
			dizionario[let] -= 1
		result.append(0)

	while dizionario['W'] > 0:
		for let in "TWO":
			dizionario[let] -= 1
		result.append(2)

	while dizionario['U'] > 0:
		for let in "FOUR":
			dizionario[let] -= 1
		result.append(4)

	while dizionario['X'] > 0:
		for let in "SIX":
			dizionario[let] -= 1
		result.append(6)

	while dizionario['O'] > 0:
		for let in "ONE":
			dizionario[let] -= 1
		result.append(1)

	while dizionario['R'] > 0:
		for let in "THREE":
			dizionario[let] -= 1
		result.append(3)

	while dizionario['F'] > 0:
		for let in "FIVE":
			dizionario[let] -= 1
		result.append(5)

	while dizionario['S'] > 0:
		for let in "SEVEN":
			dizionario[let] -= 1
		result.append(7)

	while dizionario['H'] > 0:
		for let in "EIGHT":
			dizionario[let] -= 1
		result.append(8)

	for numeroi in range(0,dizionario['I']):
		result.append(9)

#	print "RESULT:"
#	print ''.join(str(x) for x in sorted(result, key=int))

	print "Case #{}: {}".format(test, ''.join(str(x) for x in sorted(result, key=int)))