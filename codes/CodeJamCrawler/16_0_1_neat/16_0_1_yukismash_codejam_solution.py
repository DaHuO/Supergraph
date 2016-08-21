import sys

def main():
	num_test_cases = int(sys.stdin.readline())
	for i in range(num_test_cases):
		result = count_sheep(int(sys.stdin.readline()))
		if (result == -1):
			print("Case #%d: INSOMNIA" % (i + 1))
		else:
			print("Case #%d: %d" % (i + 1, result))

def count_sheep(N):
	if (N == 0):
		return -1
	i = 1
	digits = []
	while(True):
		curr_num = i * N
		for digit in str(curr_num):
			if digit not in digits:
				digits.append(digit)
				if len(digits) == 10:
					return curr_num
		i += 1
	return -1

if __name__ == "__main__":
    main()
