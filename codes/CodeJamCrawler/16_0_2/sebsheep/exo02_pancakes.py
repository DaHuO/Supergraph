def nb_moves(state):
	state = iter(state)
	last_char = next(state)
	nb_changes = 0
	for c in state:
		if c != last_char:
			last_char = c
			nb_changes += 1

	if last_char == "-":
		nb_changes += 1
	return nb_changes

with open('/tmp/out_pancakebig', "w") as out:
	n = int(input())
	for i, state in enumerate(input() for _ in range(n)):
		print("Case #%d: %d" % (i+1, nb_moves(state)), file=out)

