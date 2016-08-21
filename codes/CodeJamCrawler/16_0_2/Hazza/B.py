import sys

FLIP_LIMIT = 100000

def flip(stack, num_flip):
	flip_group = stack[:num_flip]
	bottom_group = stack[num_flip:]
	flip_group.reverse()
	for x in range(len(flip_group)):
		if flip_group[x] == "-":
			flip_group[x] = '+'
		elif flip_group[x] == "+":
			flip_group[x] = "-"

	new_stack = flip_group + bottom_group

	return new_stack

def solve_all(cases):
	cases
	for stack in cases:
		flip_count = 0
		new_stack = stack
		while True:
			if flip_count > FLIP_LIMIT:
				raise Exception("flip count limit exceeded")
			if all((x == "+" for x in new_stack)):
				break
			if all((x == "-" for x in new_stack)):
				new_stack = flip(new_stack, len(stack))
				flip_count += 1
				break
			for x in range(1, len(new_stack)):
				if new_stack[x] != new_stack[x-1]:
					new_stack = flip(new_stack, x)
					flip_count += 1
					break
		yield flip_count

if __name__ == "__main__":
    path = sys.argv[1]
    num_cases = None
    cases = []

    # Get cases
    with open(path, 'r') as f:
        try:
            num_cases = int(f.readline().strip())
        except Exception:
            raise Exception("Can't pass input file", path)
            
        for x in range(num_cases):
            cases.append(list(f.readline().strip()))

    gen = solve_all(cases)
    for x in range(num_cases):
        print "Case #%s: %s" % (x+1, gen.next())