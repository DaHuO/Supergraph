data = []
f = open('input.txt', 'r')
f.readline()
for line in f:
	data.append(int(line))

def update(x, old_set):
	new_set = old_set
	while x > 0:
		new_set = new_set - {x % 10}
		x = x / 10
	return new_set

#print data

for (test_id, n) in enumerate(data):
	cur_n = n
	digits = set(range(10))
	found = False
	#DEBUG_NUMS = []
	for i in range(1, 1000001):
		cur_n = n * i
		#DEBUG_NUMS.append(cur_n)
		digits = update(cur_n, digits)
		if len(digits) == 0:
			print 'Case #{}: {}'.format(test_id + 1, cur_n)
			found = True
			#print DEBUG_NUMS
			break
	if not found:
		print 'Case #{}: INSOMNIA'.format(test_id + 1)