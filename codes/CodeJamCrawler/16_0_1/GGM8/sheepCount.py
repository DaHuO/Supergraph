def sheepCount(input):
	n = input.splitlines()[0]

	for i in xrange(int(n)):
		num = int(input.splitlines()[i+1])
		nums = set()
		if (num == 0):
			print"Case #%d: INSOMNIA"%(i+1)
		else:
			j = 1
			while (len(nums)!=10):
				temp = num*j
				printer = temp
				while(temp!=0):
					digit = temp%10
					temp /= 10
					nums.add(digit)
				j += 1
			print"Case #%d: %d"%(i+1,printer)

