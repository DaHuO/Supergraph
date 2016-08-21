file = open("A-small-attempt2.in", 'r')
fileW = open("answer", 'w')
countTests = int(file.readline())
arrDigit = [1,2,3,5,6,7,8,9,0]
for countT in range(countTests):
	number = int(file.readline())
	tmpNumber = number	
	count = 0
	if number == 0:
		 fileW.write("Case #{}: {}\n".format(count+1,"INSOMNIA"))
		 continue

	while (len(arrDigit) != 0):
		tmpList = list(str(tmpNumber))	
		arrDigitTmp = arrDigit		
		arrDigit = []			
		for i in range (len(arrDigitTmp)):
			if not(str(arrDigitTmp[i]) in tmpList):
				arrDigit.append( arrDigitTmp[i])				
		count += 1
		tmpNumber = number * count

	fileW.write("Case #{}: {}\n".format(countT+1,number * (count-1)))
	global arrDigit
	arrDigit = [1,2,3,5,6,7,8,9,0]


