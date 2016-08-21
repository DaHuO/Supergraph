import numpy as np

no = int(input())

for i in range (1, no + 1):
	case_text = "Case #" + str(i) + ": "

	pcakes = input()
	height = len(pcakes)
	bool_stack = []

	goal = [True] * height

	for x in pcakes:
		if x == "+":
			bool_stack.append(True)
		else:
			bool_stack.append(False)

	p = 0
	flips = 0
	while bool_stack != goal:
		if p == height - 1:
			# flip above
			bool_stack = [not x for x in bool_stack[::-1]]
			flips += 1
			p = 0
		elif bool_stack[p] != bool_stack[p + 1]:
			# flip up to and including p
			bool_stack = [not x for x in bool_stack[:(p + 1)][::-1]] + bool_stack[(p + 1):]
			p += 1
			flips += 1
		else: 
			# two in a row
			# p ++
			p += 1

	print(case_text + str(flips))
			

