f = open('input.txt')
line = f.readline().split()
num_test_cases = int(line[0])
results = []

for i in xrange(num_test_cases):
	line = f.readline().split()
	N = int(line[0])
	num_list = []

	complete = False
	last_checked = 1
	for j in xrange(1, 12000):
		current_num = j * N
		last_checked = current_num

		count = 0
		while current_num > 0:
			count += 1
			current_num, r = divmod(current_num, 10)

			if r not in num_list:
				num_list.append(r)

				if len(num_list) == 10:
					complete = True
					break
		if complete:
			break
	if not complete:
		results.append("Case #" + str(i + 1) + ": " + "INSOMNIA" + '\n')
	else:
		results.append("Case #" + str(i + 1) + ": " + str(last_checked) + '\n')
f2 = open('output.txt','w')
for i in xrange(num_test_cases):
	f2.write(results[i])

