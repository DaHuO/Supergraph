t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
	n = int(input())
	seenNumbers = list()
	#print("Test case : {}: {}".format(i, n)) #to remove !!
	if(n==0):
		print("Case #{}: INSOMNIA".format(i))
	else :
		j=1
		while len(seenNumbers) != 10:
			digits = list(str(j*n))
			for digit in digits:
				if not digit in seenNumbers:
					seenNumbers.append(digit)
			#print ("j*n : {}, seenNumbers : {}".format(j*n, seenNumbers))
			j+=1
			
		print("Case #{}: {}".format(i, (j-1)*n))