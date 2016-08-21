# Code Jam 2016: Problem 1
import timeit
def sleep_routine(n):
	if n == 0:
		return "INSOMNIA"
	remaining = "0123456789"

	value = 0

	while remaining:
		value += n
		for digit in str(value):
			remaining = remaining.replace(digit, '')

	return str(value)

# Read line with the number of cases
t = int(input())
for i in range(1,t+1):
	n = int(input())
	print("Case #{}: {}".format(i, sleep_routine(n)))