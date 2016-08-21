def problem_a(N):
	if N == 0:
		return "INSOMNIA"
	complete_count = 0
	digits_found = [False] * 10
	i = 1
	while complete_count < 10:
		val = N * i
		while val:
			digit = val % 10
			if not digits_found[digit]:
				complete_count += 1
				digits_found[digit] = True
			val //= 10
		i += 1
	return str(N * (i - 1))

def read_input(filename):
	with open("output.txt", "w") as output_file:
		with open(filename) as input_file:
			T = int(input_file.readline())
			for i in range(T):
				N = int(input_file.readline())
				output_file.write("Case #{:d}: {:s}\n".format(i + 1, problem_a(N)))

read_input('A-large.in')