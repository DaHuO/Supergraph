t = int(raw_input())

for caseNumber in range(1, t + 1):
	n = int(raw_input())
	
	if n != 0:
		round = 1
		digits = set()
		
		while True:
			number_string = str(n * round)
			digits = digits.union(set(number_string))
			if len(digits) == 10:
				ans = number_string
				break
			else:
				round += 1
	else:
		ans = "INSOMNIA"
	
	print "Case #{}: {}".format(caseNumber, ans)