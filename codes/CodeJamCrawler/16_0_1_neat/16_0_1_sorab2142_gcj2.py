t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = int(raw_input())
	digitsInNum = []
	output = ""
	num = n
	for mul in xrange(1,100):
		num = mul * n;
		#print mul,",",num
		while num!=0:
			digit = num%10;
			if digit not in digitsInNum:
				digitsInNum.append(digit)
				#print mul," = ",digit
			num = num/10
		if len(digitsInNum) == 10:
			output = mul*n
			break;
	if len(digitsInNum) < 10:
		output = "INSOMNIA"
	print "Case #{}: {}".format(i, output)
# check out .format's specification for more formatting options
