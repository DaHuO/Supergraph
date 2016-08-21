n = int(input())

for i in range(n):

	strA = 'Case #%d: '%(i+1)

	delta = int(input())

	if delta == 0:
		print('Case #%d: INSOMNIA' %(i+1))
		continue

	current = 0
	board = 0

	# print(delta)

	while current < 1000000000 and board < 1023:
	# while current < 11 and board < 1023:
		current += delta
		# print(current)
		test = current
		while test > 0:
			digit = test % 10
			test = test // 10
			board = board | (1 << digit)
			# print (bin(board))

	if current >= 1000000000:
		strB = 'INSOMNIA'
	else:
		strB = '%d' %(current)

	strline = strA + strB
	print(strline)
