import sys

def main():
	num_test_cases = int(sys.stdin.readline())
	for i in range(num_test_cases):
		input = str(sys.stdin.readline())
		print("Case #%d: %s" % (i + 1, ''.join(find_last(list(input[:len(input)])))))

def find_last(S):
	if (len(S) == 1):
		return S
	curr_str = list(S[0])
	i = 1
	while(i != len(S) - 1):
		if (S[i] >= curr_str[0]):
			curr_str.insert(0, S[i])
		else:
			curr_str.insert(i, S[i])
		i += 1
	return curr_str

if __name__ == "__main__":
    main()