
import sys


def main(input_filepath):
	results = []
	with open(input_filepath, 'r') as f:
		T = int(f.readline())

		for i in range(T):
			results.append(get_final_number(int(f.readline().strip())))

	with open("counting_sheep_result.txt", "w") as f:
		for i, r in enumerate(results):
			f.write("CASE #%s: %s\n" % (i+1, r))


def get_final_number(N):
	max_iterations = 10000
	digits = []
	result = None
	for i in range(1, max_iterations):
		result = i * N
		for c in str(result):
			if c not in digits:
				digits.append(c)

		if len(digits) == 10:
			return str(result)
	return "INSOMNIA"


if __name__ == "__main__":
	main(sys.argv[1])