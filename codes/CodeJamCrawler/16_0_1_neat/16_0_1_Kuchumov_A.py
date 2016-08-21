def solve(n):
	if n == 0:
		return "INSOMNIA"
	used = set()
	delta = n
	while True:
		for c in str(n):
			used.add(c)
		if len(used) == 10:
			return n
		n += delta

def main():
	with open("input.txt", "r") as file:
		tokens = file.read().split()
	tests = int(tokens[0])
	for i in range(tests):
		n = int(tokens[i + 1])
		print('Case #{}: {}'.format(i + 1, solve(n)))

main()
