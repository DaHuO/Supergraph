
# Process the inputs into a list
def pre_process(file):

	f = open(file, 'r')

	data = list(f)

	for i in range(len(data)):

		# Get rid of the newline character
		if (data[i][-1] == '\n'):

			data[i] = data[i][:-1]

		# Get the number of test cases
		if i == 0:

			data[i] = int(data[i])

	

	return data


# Flip pancakes from i_th pancakes
def flip(pancakes, i):

	new = list(pancakes)

	for j in range(i+1):

		if new[j] == '+':

			new[j] = '-'	

		else:

			new[j] = '+'

	return "".join(new)


# Check pancakes from the bottom
def check_pancakes(pancakes):

	N = len(pancakes)

	count = 0

	for i in reversed(range(N)):

		if (pancakes[i] == '-'):

			pancakes = flip(pancakes, i)

			count = count + 1

	return count


if __name__ == "__main__":

	sol = open("./pancakes.out", "r+")

	data = pre_process("./B-large.in")

	for i in range(data[0]):

		count = check_pancakes(data[i+1])

		sol.write("Case #{}: {}\n".format(i+1, count))

	sol.close()
