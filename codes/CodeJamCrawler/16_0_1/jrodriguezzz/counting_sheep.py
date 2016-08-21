t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    if (n != 0):
        digits = set([])
        j = int(1)
        while(len(digits) < 10):
            last_num = n * j
            for digit in str(last_num):
	  	        digits.add(digit)
            j += 1
    else:
        last_num = "INSOMNIA"
    print "Case #{}: {}".format(i, last_num)