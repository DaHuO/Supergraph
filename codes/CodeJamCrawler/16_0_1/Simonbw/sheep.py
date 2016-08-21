# /usr/bin/env python3
def last_number(N):
	if N <= 0:
		return "INSOMNIA"
	digits = set()
	i = 1
	while True:
		for digit in str(N * i):
			digits.add(int(digit))
		if len(digits) == 10:
			return i * N
		i += 1

T = int(input())

for case_number in range(T):
	case_string = "Case #" + str(case_number + 1) + ":"
	N = int(input())
	print(case_string, last_number(N))
