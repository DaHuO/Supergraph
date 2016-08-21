import itertools

input_file = open('D-small-attempt1.in', 'r').readlines()
output_file = open('out-D.out', 'w')

n_inputs = int(input_file[0].strip())

for i in range(1, n_inputs+1):
	print i
	in_str = input_file[i].strip().split(" ")
	K = int(in_str[0])
	C = int(in_str[1])
	S = int(in_str[2])
	
	sequences = []
	g_indices = []
	l_indices = []
	for ind in range(K):
		g_indices.append(ind)
		all_combs = itertools.product(['L', 'G'], repeat=K)
		count = 0
		if(count == 0):
			count += 1
			continue
		for orig_seq in all_combs:
			if(count not in l_indices and ind > 0):
				continue
			orig_seq = ''.join(orig_seq)
			final_seq = orig_seq
			for i in range(1,C):
				new_seq = ""
				for tile in final_seq:
					if(tile == 'L'):
						new_seq += ''.join(orig_seq)
					elif(tile == 'G'):
						new_seq += 'G' * K
				final_seq = new_seq

			if(final_seq[ind] == 'L'):
				l_indices.append(ind)

			if(len(l_indices) == 0):
				break

	output_file.write("Case #" + str(i) + ": " + ' '.join([str(i+1) for i in g_indices]) + "\n")

	 