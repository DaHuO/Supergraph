def strip(stack):
	inStack = stack
	while stack[-1:] == '+':
		stack = stack[:-1]
	# if(inStack != stack):
		# print(stack + ' (strip)')
	return stack

def flip(stack):
	a = stack
	b = ''	
	if(a[:1] == '+'):
		# a[0] = '-'
		ind = 0
		for i in a:
			if(a[ind] == '+'):
				ind += 1
			else:
				return '-'*(ind) + a[ind:]
		




	a = a[::-1]
	flipped = ''

	for i in a :
		if(i == '+'):
			flipped += '-'
		else:
			flipped += '+'

	return flipped + b			


def solve(stack):
	count = 0;
	# print('solving : '+ stack)
	stack = strip(stack)
	i = 1
	while(len(stack) > 0):
		stack = flip(stack)
		# print(stack)
		stack = strip(stack)
		count += 1
	return count


out = ''
f = open("B-large.in",'r')
o = open("outfile.txt",'w')
i = eval(f.readline())

for n in range(i):
	stack = f.readline()
	if(stack[-1:] == '\n'):
		stack = stack[:-1]


	# print('flips: '+str(solve(stack))+'\n')
	out += 'Case #' +str(n+1) +': '+str(solve(stack))+'\n'


o.write(out[:-1])


o.close()
f.close()