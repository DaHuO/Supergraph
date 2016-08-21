

def counting_sheep(n):
	if n == 0:
		return 'INSOMNIA'
	appear_list = list()
	for i in range(10):
		appear_list.append(0)
	current_N = n
	while True:
		temp_num = str(current_N)
		for i in range(len(temp_num)):
			appear_list[int(temp_num[i])] = 1
		if min(appear_list) == 1:
			return current_N
		current_N += n


t = int(raw_input())  
for i in xrange(1, t + 1):
  n = int(raw_input())
  print "Case #{}: {}".format(i, counting_sheep(n))