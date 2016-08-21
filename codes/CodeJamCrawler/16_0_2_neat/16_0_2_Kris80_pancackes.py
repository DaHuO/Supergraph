def main():
	input = open('B-large.in')
	output = open('output.out', 'w')
	test_cases = input.readline()
	case = 0
	for stack in input:
		stack = stack.rstrip()
		case += 1
		flips = 0
		previous_pancake = stack[0]
		for pancake in stack:
			if pancake != previous_pancake:
				flips += 1
				previous_pancake = pancake
		if stack[-1] == '-':
			flips += 1
		output.write("Case #"+ str(case) + ": " + str(flips)+"\n")

if __name__ == "__main__":
	main()