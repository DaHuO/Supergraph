def pancake(fileData):


	inputData = open(fileData,'r')
	lines = inputData.readlines()
	N = int(lines[0])
	open('output.txt', 'w').close()
	outputData = open('output.txt', 'a')
	j = 1
	i = 0

	def change(string):
		newstring = ''
		for s in string:
			
			if(s == '+'):
				s = '-'
			elif(s == '-'):
				s = '+'
			newstring = newstring+s
		string = newstring[::-1]
		return(string)

	while j <= N:

		i +=1
		newstack = ''
		stack_piece = ''
		stack = lines[i]
		counter = 0
		while '-' in stack:
		
			if(stack[0] == '-' and stack[-1] == '-'):
				stack = change(stack)
				counter += 1
			elif('+' not in stack):
				stack = change(stack)
				counter += 1
			else:
				last_sign = stack[0]
				last_pos = 0
				for x in range(0,len(stack)-1):
					if(last_sign != stack[x]):
						stack_piece = stack[0:x]
						stack_piece = change(stack_piece)
						stack = stack_piece + stack[x:]
						counter += 1					
					last_sign = stack[x]
					last_pos = x
	
		print('Case #{0}: {1}'.format(j,counter))
		outputData.write('Case #{0}: {1}\n'.format(j,counter))

		j+=1

pancake('B-large.in')