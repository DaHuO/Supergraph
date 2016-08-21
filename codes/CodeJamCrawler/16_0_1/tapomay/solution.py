N = int(input())
	
def beatrix(startNum):
	
	if startNum == 0:
		return -1
		
	mul = 0
	
	detect = 0
	
	while True:
		
		if detect == 1023:
			break
		else:
			mul = mul + 1
		
		x = startNum * mul;
		
		while x != 0:
			dm = divmod(x, 10)
			x = dm[0]
			rem = dm[1]
			mask = 1 << rem
			detect = detect | mask
		
		#print(bin(detect))
	
	if detect == 1023:
		return startNum * mul
	else:
		return -1
		
for i in range(1, N+1):
	M = int(input())
	slept = beatrix(M)
	if slept == -1:
		print('Case #' + str(i) + ': ' + 'INSOMNIA')
	else:
		print('Case #' + str(i) + ': ' + str(slept))

