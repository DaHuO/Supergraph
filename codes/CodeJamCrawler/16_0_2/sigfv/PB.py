def state(pancake, flips):
	if flips % 2 == 0:
		return pancake
	return "-" if (pancake == "+") else "+"

tests = int(input())
for _ in range(tests):
	pancake_stack = str(input())
	pancakes = len(pancake_stack)
	flips = [0] * pancakes
	if pancake_stack[pancakes - 1] == "-":
		flips[pancakes - 1] = 1
	else:
		flips[pancakes - 1] = 0
	for i in range(pancakes - 2, -1, -1):
		pancake = pancake_stack[i]
		if state(pancake, flips[i + 1]) == "-":
			flips[i] = flips[i + 1] + 1
		else:
			flips[i] = flips[i + 1]
	print("Case #" + str(_ + 1) + ": " + str(flips[0]))