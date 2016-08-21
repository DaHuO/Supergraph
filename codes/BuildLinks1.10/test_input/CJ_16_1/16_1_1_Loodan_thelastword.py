
# Pre-process the inputs
def process(file):

	data = []

	f = open(file, 'r')

	temp = list(f)

	data.append(int(temp[0]))

	for i in range(1, len(temp)):

		data.append(temp[i][:-1])

	return data


def find_last(data):

	words = []

	for i in range(len(data)):

		s = list(data[i])

		ans = ""

		for c in s:

			if len(ans) == 0:

				ans = ans + c

			else:

				if c >= ans[0]:

					ans = c + ans

				else:

					ans = ans + c

		words.append(ans)

	return words



if __name__ == "__main__":

	data = process("./A-large.in")

	sol = open("./lastword.out", "r+")

	answer = find_last(data[1:])


	i = 1

	for w in answer:

		# Wrie to the solution
		sol.write("Case #{}: {}\n".format(i, w))

		i = i + 1

	sol.close()