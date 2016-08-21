filename = "B-large"

with open(filename + ".in.txt", "r") as input :
	with open(filename + ".out.txt", "w") as output :
		for case_num in range(1, int(input.readline()) + 1) :
			output.write("Case #{}: ".format(case_num))

			pan = input.readline().rstrip()
			cakes = pan[1:] + '+'

			flips = [x == y for x, y in zip(pan, cakes)].count(False)

			output.write("{}\n".format(flips))