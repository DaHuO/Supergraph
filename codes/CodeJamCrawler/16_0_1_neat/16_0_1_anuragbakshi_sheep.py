from sys import stdin

def get_digits(n):
	d = []
	while n > 0:
		d.append(n % 10)
		n //= 10

	return d

T = int(stdin.readline())

for t in range(T):
	N = int(stdin.readline())

	if N == 0:
		print("Case #{}: INSOMNIA".format(t + 1))
		continue

	digits = [False for i in range(10)]

	i = 0
	while not all(digits):
		i += 1
		x = i * N
		for d in get_digits(x):
			digits[d] = True

	print("Case #{}: {}".format(t + 1, i * N))
