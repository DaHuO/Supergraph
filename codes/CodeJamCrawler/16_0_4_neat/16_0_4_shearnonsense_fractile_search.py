from collections import deque

def gold_at_position(K, C, initial_pos, test_pos):
	gold_pos = initial_pos
	for i in range(C):
		group_length = K**(C-1-i)
		group_pos = test_pos // group_length
		test_pos -= group_pos*group_length
		if group_pos == gold_pos:
			return True
	return False

#print(gold_at_position(3, 3, 1, 12))

def fractiles(K, C, S):
	positions = deque([[a] for a in range(K)])
	final_position = None

	while positions:
		test_positions = positions.popleft()
		test_positions_ok = True
		for initial_gold_pos in range(K):
			found_gold = False
			for test_position in test_positions:
				if gold_at_position(K, C, initial_gold_pos, test_position):
					found_gold = True
					continue
				
			if not found_gold:
				# Test positions not satisfactory
				test_positions_ok = False
				break

		if test_positions_ok:
			# Test positions satisfactory
			final_position = test_positions
			break

		if len(test_positions) < S:
			max_position = test_positions[-1]
			positions.extendleft(map(lambda a: test_positions + [a], range(K, max_position, -1)))

	if final_position:
		return " ".join([str(a+1) for a in final_position])
	else:
		return "IMPOSSIBLE"

def bulk_fractiles(inp_str):
	T = 0
	output_str = ""
	for i, line in enumerate(inp_str.splitlines()):
		if i == 0:
			T = int(line)
			continue

		parts = line.split(" ")
		print("Working on %d" % i, parts)
		line_result = fractiles(int(parts[0]), int(parts[1]), int(parts[2]))
		output_str += "Case #{}: {}\n".format(i, line_result)

	return output_str

def main():
	with open("fractiles_input.txt", "r") as input_file:
		inp_str = input_file.read()
		out_str = bulk_fractiles(inp_str)
		with open("fractiles_output.txt", "w") as output_file:
			output_file.write(out_str)

main()