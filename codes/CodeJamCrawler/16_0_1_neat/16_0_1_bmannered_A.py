for tc in range(input()):
	n = raw_input()
	nint = int(n)
	if nint == 0:
		print "Case #%d: %s" % (tc + 1, 'INSOMNIA')
		continue
	multiplier = 1
 	sleepdigit0 = False
 	sleepdigit1 = False
  	sleepdigit2 = False
 	sleepdigit3 = False
 	sleepdigit4 = False
 	sleepdigit5 = False
  	sleepdigit6 = False
 	sleepdigit7 = False
  	sleepdigit8 = False
 	sleepdigit9 = False

 	while sleepdigit0 != True or sleepdigit1 != True or sleepdigit2 != True or sleepdigit3 != True or sleepdigit4 != True or sleepdigit5 != True or sleepdigit6 != True or sleepdigit7 != True or sleepdigit8 != True or sleepdigit9 != True: 
 		max_count = nint * multiplier
 		digits = [int(i) for i in str(max_count)]
 		multiplier += 1
 		for ch in digits:
 			if ch == 0:
 				sleepdigit0 = True
 			if ch == 1:
 				sleepdigit1 = True
 			if ch == 2:
 				sleepdigit2 = True
 			if ch == 3:
 				sleepdigit3 = True
 			if ch == 4:
 				sleepdigit4 = True
 			if ch == 5:
 				sleepdigit5 = True
 			if ch == 6:
 				sleepdigit6 = True
 			if ch == 7:
 				sleepdigit7 = True
 			if ch == 8:
 				sleepdigit8 = True
 			if ch == 9:
 				sleepdigit9 = True
	print "Case #%d: %s" % (tc + 1, max_count)