def ishappy(bool_array):
	for el in bool_array:
		if not el:
			return False
	return True

# Number of test cases
t = int(raw_input())

for i in xrange(1, t+1):
 	raw = raw_input()
 	bool_array = list()
 	for car in raw:
 		if car == '+':
 			bool_array.append(True)
 		else:
 			bool_array.append(False)

 	counter = 0
 	array_size = len(bool_array)

 	if array_size == 1:
 		if bool_array[0] == True:
			print "Case #{}: {}".format(i, 0)
		else:
			print "Case #{}: {}".format(i, 1)
	else:
	 	while not ishappy(bool_array):
	 		#print bool_array
	 		if bool_array[0]:
	 			counter += 1
	 			for j in range(0, array_size):
	 				if bool_array[j] == True:
	 					bool_array[j] = False
	 				else:
	 					break
	 		else: #bool_array == False
	 			counter += 1
	 			for j in range(0, array_size):
	 				if bool_array[j] == False:
	 					bool_array[j] = True
	 				else:
	 					break	
		print "Case #{}: {}".format(i, counter)

