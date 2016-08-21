import sys

lines = [x for x in open(sys.argv[1], 'rt').readlines()]
count = int(lines.pop(0))
with open('out.txt', 'wt') as outfile:
	for i in xrange(count):
		parties_dict = {}
		parties_count = int(lines.pop(0))
		parties_list = [int(x) for x in lines.pop(0).split()]
		#for party_ind in xrange(parties_count):
		#	parties_dict[party_ind + 1] = int(parties_list[party_ind])
		res = []
		while sum(parties_list) > 0:
			major = sum(parties_list) / 2
			if sum(parties_list) % 2 == 0:
				major += 1

			#dist_from_major = []
			#for i in parties_list:
			#	dist_from_major.append(major - i)
			temp_res = []
			amount_to_remove = 2
			if sum(parties_list) == 3:
				amount_to_remove = 1
			for k in xrange(amount_to_remove):
				max_dist = max(parties_list)
				remove_from = [k for k in xrange(len(parties_list)) if parties_list[k] == max_dist][:1]
				parties_list[remove_from[0]] -= 1
				temp_res.append(chr(65 + remove_from[0]))

			res.append(temp_res)

		print 'Case #%d: %s' % (i + 1, ' '.join(''.join(x) for x in res))
		outfile.write('Case #%d: %s\n' % (i + 1, ' '.join(''.join(x) for x in res)))
	