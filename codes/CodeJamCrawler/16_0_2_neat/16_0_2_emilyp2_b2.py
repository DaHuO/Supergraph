def flip_part(sl):
	if sl == '+-':
		return '--'
	elif sl == '-+':
		return '++'

	n = ''
	for d in sl:
		if d == '+':
			n += '-'
		elif d == '-':
			n += '+'
	print n
	n = n[::-1]
	print n + '\n\n'
	return n

def find_co(stack):
	m = stack[0]
	for i in range(1, len(stack)):
		if stack[i] != m:
			return i

	return 0

def flip_first(stack):
	if stack == '-'*len(stack):
		return '+'*len(stack)

	co = find_co(stack)
	print co
	stackl = stack[:co]
	stackr = stack[co:]

	if stackl:
		stackl = flip_part(stackl)

	print(stackl + stackr)
	return stackl + stackr


fi = open('B-large.in', 'r')
fo = open('b2.out', 'w')

T = fi.readline()
T = int(T)

for x in range(1,T+1):
	stack = fi.readline().rstrip()
	flips = 0
	digit = 1

	print (stack + ': ')

	fo.write('Case #'+str(x)+': ')

	while (stack != '+'*len(stack)):
		stack = flip_first(stack)
		flips += 1

	fo.write(str(flips) + '\n')

fi.close()
fo.close()

