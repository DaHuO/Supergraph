def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('C-small-attempt1.in', 'r'), open('C-small-attempt1.out', 'w')

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	N = int(in_file.readline())
	F = [int(i) for i in in_file.readline().split()]
	best_friends = {}
	for i in range(len(F)):
		best_friends[i+1] = F[i]
	two_el_cycles = []
	for k, v in best_friends.items():
		if k == best_friends[v]:
			two_el_cycles.append((k, v))

	# FORM GROUPS
	groups = []
	special_groups = []
	traversed = []
	in_group = []
	for f in best_friends.keys():
		if f in traversed:
			continue
		curr = f
		group = []
		add = True
		while curr not in group:
			if curr in in_group:
				add = False
				break
			traversed.append(curr)
			group.append(curr)
			curr = best_friends[curr]
		if len(group) >= 2 and (group[-1], group[-2]) in two_el_cycles:
			special_groups.append(group)
		elif add:
			in_group.extend(group)
			groups.append(group)
	
	# DELETE UNNNEEDED SPECIAL GROUPS
	d = {}
	new_special_groups = []
	for group in special_groups:
		if (group[-1], group[-2]) not in d:
			d[(group[-1], group[-2])] = [group]
		else:
			d[(group[-1], group[-2])].append(group)
	for k, v in d.items():
		ml = max([len(group) for group in v])
		for group in v:
			if len(group) == ml:
				new_special_groups.append(group)
				break
	special_groups = new_special_groups


	# CONSOLIDATE SPECIAL GROUPS
	total_special_length = 0
	while True:
		max_length = 0
		max_groups = None
		for i in range(len(special_groups)):
			for j in range(i+1, len(special_groups)):
				if (special_groups[i][-1], special_groups[i][-2]) == (special_groups[j][-2], special_groups[j][-1]):
					group_length = len(special_groups[i]) + len(special_groups[j]) - 2
					if group_length > max_length:
						max_length = group_length
						max_groups = (i, j)
		if max_groups is None:
			break
		else:
			total_special_length += max_length
			special_groups.pop(max_groups[1])
			special_groups.pop(max_groups[0])

	if special_groups != [] and total_special_length == 0:
		total_special_length = max([len(group) for group in special_groups])
	
	if groups == []:
		max_circle_size = total_special_length
	elif special_groups == []:
		total_normal_length = max([len(group) for group in groups])
		max_circle_size = total_normal_length
	else:
		max_circle_size = max(total_normal_length, total_special_length)
	epilogue(str(max_circle_size), case_num)





