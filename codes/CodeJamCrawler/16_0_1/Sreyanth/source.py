def read():
	return int(raw_input())
	
t= read()

runs = 10

for i in range(t):
	digits = []
	run = 1
	number = read()
	n = number
	while True:
		for j in str(number):
			if j not in digits:
				digits.append(j)
		if len(digits) == 10:
			print "Case #%d: %d" % (i+1, number)
			break
		run += 1
		if run == 500:
			print "Case #%d: INSOMNIA" % (i+1)
			break
		else:
			number = (run)*n