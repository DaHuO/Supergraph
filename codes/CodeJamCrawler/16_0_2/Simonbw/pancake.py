# /usr/bin/env python3
T = int(input())

UP = '+'
DOWN = '-'

for case_number in range(T):
	case_string = "Case #" + str(case_number + 1) + ":"
	pancakes = input()

	flips = 0
	current = pancakes[0]
	for pancake in pancakes:
		if pancake != current:
			flips += 1
		current = pancake
	if current == DOWN:
		flips += 1
	print(case_string, flips)
