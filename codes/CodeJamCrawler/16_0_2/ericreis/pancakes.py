# stack is a vector of pancakes
def pancake(stack, counter):
	# print stack
	if len(stack) == 0:
		return counter
	if stack[-1] == "+":
		return pancake(stack[:-1], counter)
	else:
		if stack[0] == "+":
			numberOfPlus = 0
			for e in stack:
				if e == "+":
					numberOfPlus += 1
				else:
					break
			stack[:numberOfPlus] = ["-"] * numberOfPlus		
		else:
			stack = flip(stack)
		counter += 1
		return pancake(stack, counter)	



def flip(stack):
	for i in xrange((len(stack) + 1) / 2):	
		stack[i], stack[-(i + 1)] = reverse(stack[-(i + 1)]), reverse(stack[i])
	return stack



def reverse(elem):
	if elem == "+":
		return "-"
	if elem == "-":
		return "+"


def main():
	t = int(input())

	for i in xrange(1, t + 1):
		sequence = raw_input()

		stack = list(sequence)

		print("Case #{}: {}".format(i, pancake(stack, 0)))



main()

# print pancake(list("-+-+-+----"), 0)

# print flip(list("+-"))
