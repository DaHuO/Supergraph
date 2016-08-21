t = int(raw_input())


for i in xrange(1, t + 1):

	n = int(raw_input())

	if  n == 0:
		print "Case #{}: INSOMNIA".format(i)
		continue

	array = [0,1,2,3,4,5,6,7,8,9]
	for ij in  range( 0 , len(array) ):
		array[ij] = 0

	j = 1

	while True:
		number = n * j
		temp = str(number)

		#print temp

		for k in temp:
			array[int(k)] = 1

		#print array

		flg = 1

		for ar in  array:
			if ar == 0:
				flg = 0
				break;

		if flg == 1:
			print "Case #{}: {}".format(i, number)
			break

		else:
			j = j + 1



  