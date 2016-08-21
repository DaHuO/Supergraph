def solve(x):
	count = 0
	startNumber = x

	digits = [False, False, False, False, False, False, False, False, False, False]

	loop = 0
	res = ""
	if startNumber == 0:
		res = "INSOMNIA"
	else:
		while count < 10:
			loop += 1
			number = startNumber * loop
			numberString = str(number)
			for i in range (0,len(numberString)):
			
				theNumber = int(numberString[i])
				if not digits[theNumber]:
					digits[theNumber] = True
					count += 1
			
		res = str(loop * startNumber)

	return res
	

T = int(raw_input())
for t in range(T):
	n = int(raw_input())
	
	print 'Case #' + str(t+1) + ': ' + solve(n)
