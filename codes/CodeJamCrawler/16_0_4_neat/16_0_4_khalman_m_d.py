data = []
f = open('input.txt', 'r')
f.readline()
for line in f:
	data.append(line)

#print data

for (test_id, s) in enumerate(data):
	splited = s.split()
	k, c, s = int(splited[0]), int(splited[1]), int(splited[2])
	if s * c < k:
		print 'Case #{}: IMPOSSIBLE'.format(test_id + 1)
		continue
	print 'Case #{}: '.format(test_id + 1),
	id_to_check = 0
	checked_all = False
	for i in xrange(s):
		cur_ans = 0
		for j in xrange(c):
			cur_ans = cur_ans * k + id_to_check
			id_to_check = id_to_check + 1
			if id_to_check == k:
				id_to_check = k - 1
				checked_all = True
		print '{} '.format(cur_ans + 1),
		if checked_all:
			break
	print 