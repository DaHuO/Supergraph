filename = "D-small-attempt0"

with open(filename + ".in.txt", "r") as input :
	with open(filename + ".out.txt", "w") as output :
		for case_num in range(1, int(input.readline()) + 1) :
			output.write("Case #{}: ".format(case_num))

			k, c, s = map(int, input.readline().split())

			if (s < k) :
				output.write("IMPOSSIBLE\n")
				continue
			
			solution = " ".join(map(str, range(1, s+1)))
			output.write("{}\n".format(solution))