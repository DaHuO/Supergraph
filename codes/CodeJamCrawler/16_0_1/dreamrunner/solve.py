__author__ = "Xinzi Zhou"
__email__ = "imdreamrunner@gmail.com"


def digits(n):
	return (int(d) for d in str(n))


def solve(n):
	if not n:
		return "INSOMNIA"
	bag = set()
	i = 1
	while len(bag) < 10:
		bag = bag.union(digits(n * i))
		i += 1
	return n * (i - 1)


def main():
	num_of_test = int(input())

	for test_id in range(1, num_of_test + 1):
		n = int(input())
		print("Case #" + str(test_id) + ": " + str(solve(n)))

if __name__ == "__main__":
	main()
