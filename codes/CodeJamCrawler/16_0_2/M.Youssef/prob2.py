#Prob 2
caseNumber = 0
with open('input2.txt','r') as file:
	for pancakeTower in file:
		firstTime = 1
		signChanges = 0
		#Reverse and add + at the beginning
		pancakeTowerReversed = pancakeTower[::-1]
		pancakeTowerReversed.rstrip()
		#print("PanckageTower =====>" + pancakeTowerReversed)
		initialSign = "+"
		
		#print(pancakeTowerReversed)
		for sign in pancakeTowerReversed:
			if(firstTime):
				firstTime = 0
			else:
				if(initialSign != sign):
					#print("SignChange --->" + sign)
					initialSign = sign
					signChanges = signChanges + 1
		caseNumber = caseNumber + 1
		print("Case #" + str(caseNumber) + ": " +str(signChanges))