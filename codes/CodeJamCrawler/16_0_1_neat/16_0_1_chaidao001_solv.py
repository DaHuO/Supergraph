def solve(number):

	if number == 0:
		return "INSOMNIA"

	i = 1

	numberSet = set()

	while True:

		value = number * i

		print(value)

		for n in str(value):
			numberSet.add(n)

			if len(numberSet) == 10:
				return str(i * number)

		i += 1


	return "INSOMNIA"


input_file_name = "A-large.in"
output_file_name = "output.out"


with open(input_file_name, "r") as input:
	number_cases = int(input.readline())

	with open(output_file_name, "w") as output:

		for i in range(number_cases):

			result = solve(int(input.readline()))

			if result is None:
				print("NOOOOOOOO")
			else:
				output.write("Case #" + str(i + 1) + ": " + result + "\n")
