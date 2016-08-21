def calculate(num, case, output):
	increment = 1
	found = False
	digits = set()	
	while not found:
		number = num * increment		
		while number > 0:
			digit = number % 10
			digits.add(digit)
			number = int(number/10)
			if len(digits) == 10:
				output.write("Case #" + str(case) + ": " + str(num*increment) + '\n')
				found = True
				break
		increment = increment + 1

def main():
	input = open('A-large.in')
	output = open('output.out', 'w')
	test_cases = input.readline()
	case = 0
	numbers = [int(i) for i in input]
	for num in numbers:
		case += 1
		if num == 0:
			output.write("Case #" + str(case) + ": INSOMNIA\n")
			continue
		calculate(num, case, output)	
	

if __name__ == "__main__":
	main()