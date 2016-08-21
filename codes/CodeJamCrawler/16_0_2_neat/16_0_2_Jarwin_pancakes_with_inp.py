#!/usr/bin/env python
test_case = 0

def flip(l):
	global counter
	counter = counter + 1
	l.reverse()
	rl = []
	for n in l:
		if n == '+':
			rl.append('-')
		if n == '-':
			rl.append('+')
	return rl

while True:
	try:
		pancake_stack = raw_input().strip()
		if test_case == 0:
			test_case=1;continue
		check_with = list(pancake_stack.replace('-','+'))
		pancake_stack = list(pancake_stack)
		counter = 0
		while True:
			index =0
			try:
				index = pancake_stack.index('+')
			except ValueError:
				pancake_stack = flip(pancake_stack)
				if pancake_stack == check_with:
					print "Case #{}: {}".format(test_case,counter)
					break
			if index == 0:
				try:
					index = pancake_stack.index('-')
				except ValueError:
					print "Case #{}: {}".format(test_case,counter)
					break
			left = pancake_stack[:index]
			left = flip(left)
			pancake_stack = left + pancake_stack[index:]
			
		test_case+=1
	except EOFError:
		exit()