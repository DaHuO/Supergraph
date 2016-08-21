T = input()
values = []
for z in range(T):
	values.append(input())

count = 1

for i in values:
	current = i
	current_const = current
	num_list = []
	while(True):
		str_current = str(current)
		if(current == 0):
			print "Case #{}: {}".format(count, "INSOMNIA")
			break
		
		for j in str_current:
			if j not in num_list:
				num_list.append(j)
		if(len(num_list)==10):
			print "Case #{}: {}".format(count, str_current)
			break
		current += current_const
	count += 1
