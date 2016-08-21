import fileinput

t = int(raw_input())
for i in range(0, t):
	n = int(raw_input())
	toAdd = n
	sofar = {}
	digits = [0] * 10
	found = False
	while(sofar.has_key(n) == False):
		sofar[n] = 1
		digis = n
		while (digis > 0):
			digits[digis%10] = 1
			digis = digis/10
		sum = 0
		for j in range(0, 10):
			sum = sum + digits[j]
		if (sum == 10):
			found = True
			break;	
		n = n + toAdd
	if (found):
		print "Case #" + str(i+1) + ": " + str(n)
	else:
		print "Case #" + str(i+1) + ": INSOMNIA"
		
