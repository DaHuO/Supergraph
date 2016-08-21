"""Problem A. The Last Word

		Miguel Angel Rivera Notararigo (ntrrg) <ntrrgx@gmail.com>
"""

input = open("A-small-attempt0.in")
output = open("output", "w")

T = int(input.readline())
assert T >= 1 and T <= 100

n = 1

while T > 0:
	S = input.readline().strip()
	lS = len(S)
	assert lS >= 1 and lS <= 15

	lw = []

	lw.append(S[0])

	for letter in S[1:]:
		nlw = []

		for word in lw:
			nlw.append(letter + word)
			nlw.append(word + letter)

		lw = nlw[:]

	lw.sort()

	output.write("Case #{}: {}\n".format(n, lw[-1]))
	T -= 1
	n += 1

input.close()
output.close()