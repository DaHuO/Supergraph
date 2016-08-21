from itertools import product

N = 16
J = 50

wo11 = product([0, 1], repeat=N-2)
possiblecoins = []
numgoodcoins = 0
print "Case #1:"
for p in wo11:
	possiblecoins.insert(len(possiblecoins), ''.join(map(str, p)))
for q in possiblecoins:
	possiblecoins[possiblecoins.index(q)] = int('1' + q + '1')
for coin in possiblecoins:
	nontrivials = ''
	numnons = 0
	for base in range(2,11):
		b10 = int(str(coin), base)
		for divisor in range(2, int(b10**0.5)+2):
			if b10 % divisor == 0:
				nontrivials += ' ' + str(divisor)
				numnons += 1
				break
		if numnons == 9:
			numgoodcoins += 1
			print str(coin) + nontrivials
	if numgoodcoins == J:
		break
