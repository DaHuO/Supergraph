def main(N):
	i = 0
	digits_seen = set()
	while len(digits_seen) < 10:
		i += 1
		num = N * i
		if num == 0:
			return "INSOMNIA"
		record_digits(num, digits_seen)
	return num


def record_digits(num, memo):
	for char in str(num):
		memo.add(char)

if __name__ == "__main__":
	input_file = "A-large.in"
	output_file = "partA_LARGE_output.txt"
	with open(input_file, 'rb') as f:
		with open(output_file, 'wb') as o:
			T = f.readline()
			for i, line in enumerate(f):
				answer = main(int(line))
				o.write("Case #" + str(i + 1) + ": " + str(answer) + "\n")