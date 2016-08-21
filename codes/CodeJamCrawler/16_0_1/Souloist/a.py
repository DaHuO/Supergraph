def sleep_count(w):
	iteration = 1
	array = []

	if w == 0:
		return "INSOMNIA"

	while True:
		new = str(iteration*w)

		for i in list(new):
			if i not in array:
				array.append(i)
		
		if sorted(array) == ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']:
			return new

		iteration+=1

test_number = str(raw_input())

for i in range(int(test_number)):
	test = int(raw_input())
	print "Case #"+str(i+1) + ": " + str(sleep_count(test))		