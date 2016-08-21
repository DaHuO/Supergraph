f = open('A-large.in.txt', 'r')
T = int(f.readline())

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for t in range(0,T):
	N = int(f.readline()) # number of political parties
	parties = map(int, f.readline().split()) # senators in each party

	plan = []

	while True:
		if max(parties) == 0:
			break
		# print(parties)

		nonzero = []
		indexes = []
		for i in range(0,len(parties)):
			if parties[i] != 0:
				nonzero.append(parties[i])
				indexes.append(i)

		if len(nonzero) == 2:
			if nonzero[0] == nonzero[1]:
				plan.append(alphabet[indexes[0]] + alphabet[indexes[1]])
				parties[indexes[0]] -= 1
				parties[indexes[1]] -= 1
				continue

		maxi = 0
		index = 0
		for i in range(0,len(parties)):
			if parties[i] > maxi:
				maxi = parties[i]
				index = i
		# print(maxi)
		# print(index)
		letter = alphabet[index]
		plan.append(letter)
		parties[index] -= 1

	output = ''
	for p in plan:
		output += p
		output += ' '
	output = output[:-1]

	# print(output)
	# output = output[:len(output)-2] + output[len(output)-1:]
	# print(output)

	print('Case #' + str(t+1) + ': ' + output)
	
f.close()