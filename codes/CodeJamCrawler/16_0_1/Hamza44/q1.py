t = int (raw_input())
for i in xrange(1,t+1):
	arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]	
	n = int(raw_input())
	num = n
	num1 = n
	j = 1
	if num1 is 0:
		num1 = "INSOMNIA"
	else:
		while len(arr) > 0:
			number = num % 10
			num = num / 10
			if number in arr:
				arr.remove(number)
				if len(arr) is 0:
					break
			if num is 0:
				j = j+1
				num = n*(j)
				num1 = num
	print "Case #{}: {}".format(i, num1)