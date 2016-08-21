def get_num_flips(pancakes):
	num_flips = 0

	if len(pancakes) == 0:
		return 0
	elif len(pancakes) == 1:
		return 1 if pancakes == "-" else 0

	# 1 flip for every transition
	for i in xrange(len(pancakes) - 1):
		if pancakes[i] != pancakes[i+1]:
			num_flips += 1

	# 1 flip if last value is (-)
	if pancakes[-1] == "-":
		num_flips += 1

	return num_flips

num_cases = int(raw_input())

for i in xrange(num_cases):
	pancakes = raw_input()
	num_flips = get_num_flips(pancakes)

	print("Case #" + str(i + 1) + ": " + str(num_flips))