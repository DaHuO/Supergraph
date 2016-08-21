filename = "A-large"

with open(filename + ".in.txt", "r") as input :
	with open(filename + ".out.txt", "w") as output :
		for case_num in range(1, int(input.readline()) + 1) :
			output.write("Case #{}: ".format(case_num))

			n = int(input.readline())

			if (n == 0) :
				output.write("INSOMNIA\n")
				continue

			acc = 0
			seen = set()

			while (len(seen) < 10) :
				acc += n
				seen |= set(str(acc))

			output.write("{}\n".format(acc))