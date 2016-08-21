def getDigits(digits,n):
	number_string = str(n)
	for x in number_string:
		digits[int(x)] = 1
	return digits



if __name__ == '__main__':
	M = int(raw_input())
	

	for j in range(M):
		
		N = int(raw_input())
		
		if N == 0:
			print "Case #"+str(j+1)+": INSOMNIA"
		
		else:
			digits = [0 for _ in range(10)]
		
			for i in range(1,91):	
		
				digits = getDigits(digits,i*N)
		
				if sum(digits) == 10:
					print "Case #"+str(j+1)+": "+str(i*N)
					break
		
			if sum(digits) != 10:
				print "Case #"+str(j+1)+": INSOMNIA"







