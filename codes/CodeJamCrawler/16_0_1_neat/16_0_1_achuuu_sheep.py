f = open('A-large.in', 'r')

T = f.readline()

output = open("sheep.txt", 'w')

i = 1
for line in f:
	digits = [False,False,False,False,False,False,False,False,False,False]
	count = 0
	N = int(line[:-1])
	if N == 0:
		output.write('Case #' + str(i) + ': INSOMNIA\n')
	else:
		m = 1
		while count < 10:
			curr = m * N
			for c in str(curr):
				if not digits[int(c)]:
					digits[int(c)] = True
					count = count + 1
			m = m + 1
		m = m - 1
		output.write('Case #' + str(i) + ': ' + str(m*N) + '\n')
	i = i + 1