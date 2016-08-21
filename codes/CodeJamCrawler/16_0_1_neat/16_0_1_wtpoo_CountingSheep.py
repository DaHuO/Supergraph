T = int(raw_input().strip()) 
digits = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for z in range(0, T):
	line = raw_input().strip()
	input = int(line)
	seen_digits = set([int(i) for i in line.strip()])
	#print "seen_digits" + str(seen_digits)
	unseen_digits = digits - seen_digits
	#print "unseen_digits" + str(unseen_digits)
	seen_digits1 = seen_digits
	j = 2
	while True:
		seen_digits = set([int(i) for i in str(j*input)])
		if input == 0:
			print("Case #%d: "%(z+1)+"INSOMNIA")
			break
		unseen_digits = unseen_digits - seen_digits
		seen_digits1 = seen_digits
		#print "unseen_digits" + str(unseen_digits)
		if len(unseen_digits) == 0:
			print "Case #%d: "%(z+1)+str(j*input)
			break
		j = j+1
