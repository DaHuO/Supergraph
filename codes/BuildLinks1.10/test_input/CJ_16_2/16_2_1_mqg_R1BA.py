#2016 GCJ 1BA


import sys



n = int(input())

for i in range(n):
	strline = raw_input()

	charlist = list()

	board = dict()
	counter = [0] * 10

	for c in strline:
		if board.has_key(c):
			board[c] += 1
		else:
			board[c] = 1

	if board.has_key('Z'):
		counter[0] = board['Z']

	if board.has_key('X'):
		counter[6] = board['X']

	if board.has_key('W'):
		counter[2] = board['W']

	if board.has_key('U'):
		counter[4] = board['U']

	if board.has_key('G'):
		counter[8] = board['G']

	if board.has_key('F'):
		counter[5] = board['F'] - counter[4]

	if board.has_key('H'):
		counter[3] = board['H'] - counter[8]

	if board.has_key('O'):
		counter[1] = board['O'] - counter[0] - counter[2] - counter[4]

	if board.has_key('S'):
		counter[7] = board['S'] - counter[6]

	if board.has_key('N'):
		counter[9] = board['N'] - counter[1] - counter[7]
		counter[9] /= 2
	
	numlist = list()
	for k in range(10):
		for j in range(counter[k]):
			numlist.append(k)

	strA = 'Case #%d: '%(i+1)
	strB = "".join(str(x) for x in numlist)

	printstr = strA + strB
	print(printstr)
