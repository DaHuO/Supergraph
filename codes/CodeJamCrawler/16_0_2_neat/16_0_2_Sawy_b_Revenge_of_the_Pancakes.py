def problem_B():
	T = int(raw_input().strip()) + 1
	for t in range(1, T):
		flips_count = 0
		#Load a list with all the files
		stack = list(raw_input().strip())
		fliped_stack = []
		ready_to_flip = False
		flipped = True
		
		while(flipped):
			flipped = False
			ready_to_flip = False
			pointer = -1 #reset the pointer
			for pancake in stack:
				if ready_to_flip and pancake == '+':
					#flip
					break
				if pancake == '-':
					ready_to_flip = True
				pointer+=1
			if ready_to_flip:
				for i in range(pointer+1):
					stack[i] = '-' if stack[i] == '+' else '+'
				flips_count+=1
				flipped = True
					
		print 'Case #{0}: {1}'.format(t, flips_count)