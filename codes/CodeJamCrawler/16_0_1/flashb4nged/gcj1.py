

def solve_A(N):
	if N == 0:
		return "INSOMNIA"
	current = N
	digits = set([])
	while len(digits) < 10:
		digits.update([int(i) for i in str(current)])
		current = current+N
	return current-N


def main():
	number_of_samples = int(input())
	for i in range(1, number_of_samples + 1):
		N = int(input())
		print("Case #{}: {}".format(i,solve_A(N)))



if __name__ == '__main__':
	main()