def flip_orientation(o):
	return "-" if o == "+" else "+"

def flipped(pancakes):
	result = ""
	for p in pancakes:
		result = flip_orientation(p) + result
	return result

def best_flips(pancakes, required_orientation="+", just_flipped=False):
	if len(pancakes) == 0:
		return 0

	# let W be wrong orientation, C be correct orientation
	if pancakes[-1] == required_orientation:
		# Last pancake C, so we can ignore it and work with the rest
		return best_flips(pancakes[:-1], required_orientation=required_orientation, just_flipped=False)
	
	# last pancake W
	# We can either make all previous pancakes W and then flip, 
	# if we haven't just flipped we could flip and then make all C

	flip_last = 1 + best_flips(pancakes[:-1], required_orientation=flip_orientation(required_orientation), just_flipped=False)

	if just_flipped:
		return flip_last
	else:
		flip_first = 1 + best_flips(flipped(pancakes), required_orientation=required_orientation, just_flipped=True)
		return min(flip_first, flip_last)

def bulk_best_flips(inp_str):
	T = 0
	output_str = ""
	for i, line in enumerate(inp_str.splitlines()):
		if i == 0:
			T = int(line)
			continue

		line_result = best_flips(line)
		output_str += "Case #{}: {}\n".format(i, line_result)

	return output_str

with open("revenge_of_the_pancakes_input.txt", "r") as input_file:
	inp_str = input_file.read()
	out_str = bulk_best_flips(inp_str)
	with open("revenge_of_the_pancakes_output.txt", "w") as output_file:
		output_file.write(out_str)