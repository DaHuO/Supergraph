

def last_num(n):
	if n == 0:
		return "INSOMNIA"
	not_seen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	curr = n
	while (len(not_seen) > 0):
		for digit in str(curr):
			try:
				not_seen.remove(digit)
			except ValueError:
				pass
		curr += n
	return curr - n

def main():
	# take in input
	t = int(raw_input())

	solutions = []

	for i in range (t):
		n = int(raw_input())
		solutions.append("Case #" + str(i+1) + ": " + str(last_num(n)))

	for solution in solutions:
		print solution


if __name__ == "__main__":
	main()