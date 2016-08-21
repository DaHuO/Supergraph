start = int(input());

for T in range(start):

	takeNumber = int(input());
	allNums = ["1","2","3","4","5","6","7","8","9","0"];
	count = 1;
	while (count > 0):
		newNumber = str(takeNumber*count);
		for x in range(len(newNumber)):
			
			if newNumber[x] in allNums:
				allNums.remove(newNumber[x])
				req = newNumber;

		count+=1;
		if not allNums:
			break;

		elif takeNumber == 0:
			req = "INSOMNIA";
			break;

	print ("Case #%s: %s" %((T + 1), req))

		
