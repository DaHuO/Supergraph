LOG_FILE = "B-large.in"

with open(LOG_FILE) as f:
	data = f.readlines()

ntimes = int(data[0])
for ntry in range(ntimes):
	line = data[ntry + 1].strip()
	stack_size = len(line)
	# print stack_size
	cur_side = line[0]
	n_changes = 0
	for i in range(1, stack_size):
		if line[i] != cur_side:
			cur_side = line[i]
			n_changes += 1
	if cur_side == "-":
		n_changes += 1
	print "Case #" + str(ntry + 1) + ":", str(n_changes)