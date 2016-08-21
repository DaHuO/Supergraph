"""Problem A. Counting Sheep
		Miguel Angel Rivera Notararigo (ntrrg) <ntrrgx@gmail.com>
"""

input = open("A-large.in")
output = open("output", "w")

T = int(input.readline())

assert T >= 1 and T <= 100

t = 1

while T > 0:
	N = int(input.readline())

	assert N >= 0 and N <= 10 ** 6

	numbers = []
	i = 1

	while len(numbers) < 10:
		r = N * i

		if not r:
			r = "INSOMNIA"
			break

		for n in str(r):
			if not n in numbers:
				numbers.append(n)

			if len(numbers) >= 10:
				break

		i += 1

	output.write("Case #%i: %s\n" % (t, r))

	T -= 1
	t += 1

input.close()
output.close()