def all_happy(x):
	return '-' not in x

def all_sad(x):
	return '+' not in x

def find_first_opp(x):
	sign = x[0]

	for i, val in enumerate(x):
		if val != sign:
			return i
	else:
		return -1

def reverse_sign(val):
	return '+' if val == '-' else '-'

def flip_till_opposite(x, opp):
	dup_x = list(x)

	for i in range(0, opp):
		dup_x[i] = reverse_sign(x[i])

	return "".join(dup_x)

def min_flips(x):
	count = 0

	while not all_happy(x):
		if all_sad(x):
			return count + 1
		first_opposite = find_first_opp(x)
		x = flip_till_opposite(x, first_opposite)
		count = count + 1

	return count

def main():
	cases = int(input())
	counter = 0

	while counter < cases:
		counter = counter + 1
		x = input()
		print("Case #{x}: {y}".format(x=counter, y=min_flips(x)))

main()