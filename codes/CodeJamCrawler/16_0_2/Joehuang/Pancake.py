def flip(li):
	c_layer = 0
	c_val = li[c_layer]
	flip_count = 0
	while c_layer is not len(li)-1:
		if li[c_layer+1] is not c_val:
			flip_count += 1
			c_val = li[c_layer+1]
		c_layer += 1
	if c_val is not 1:
		flip_count += 1
	return flip_count





num_input = int(raw_input())  # read a line with a single integer
for j in xrange(1, num_input + 1):
    string = raw_input()
    List = []
    for i in range(len(string)):
    	val = string[i]
    	if val == '+':
    		List.append(1)
    	else:
    		List.append(0)
    flip_num = flip(List)
    print "Case #{}: {}".format(j, flip_num)