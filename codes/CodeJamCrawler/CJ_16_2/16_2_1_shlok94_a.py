T = int(raw_input())

for i in range(T):
	string = list(raw_input().lower())
	no = []
	# print 'here'
	# print string
	while(len(string)):
		# print 'string', string
		# print 'no', no
		if 'z' in string:
			no.append('0')
			string.remove('z')
			string.remove('e')
			string.remove('r')
			string.remove('o')

		elif 'w' in string:
			no.append('2')
			string.remove('t')
			string.remove('w')
			string.remove('o')

		elif 'u' in string:
			no.append('4')
			string.remove('f')
			string.remove('u')
			string.remove('r')
			string.remove('o')


		elif 'x' in string:
			no.append('6')
			string.remove('s')
			string.remove('i')
			string.remove('x')

		elif 'g' in string:
			no.append('8')
			string.remove('e')
			string.remove('i')
			string.remove('g')
			string.remove('h')
			string.remove('t')


		elif 'o' in string:
			no.append('1')
			string.remove('n')
			string.remove('e')
			string.remove('o')

		elif 't' in string:
			no.append('3')
			string.remove('t')
			string.remove('e')
			string.remove('r')
			string.remove('h')
			string.remove('e')

		elif 'f' in string:
			no.append('5')
			string.remove('f')
			string.remove('e')
			string.remove('i')
			string.remove('v')

		elif 'v' in string:
			no.append('7')
			string.remove('s')
			string.remove('e')
			string.remove('v')
			string.remove('n')
			string.remove('e')

		elif 'i' in string:
			no.append('9')
			string.remove('n')
			string.remove('e')
			string.remove('i')
			string.remove('n')

	no.sort()
	print 'Case #'+str(i+1)+': '+''.join(no)



