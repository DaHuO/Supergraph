def findDigits(number,digitsKnown):
	for j in range(len(str(number))):
		lastDigit = number%10
		if lastDigit not in digitsKnown:
			digitsKnown.append(lastDigit)
		number = number//10
for i in range(int(input())):
	number = int(input())
	digitsKnown = []
	findDigits(number,digitsKnown)
	number2 = int(number)
	number = int(number)
	
	while len(digitsKnown) < 10:
		findDigits(number2,digitsKnown)
		number2 += number
		answer = str(number2-number)
		if number == 0:
			answer = "Insomnia"
			break
	print("Case #"+str(i+1) +": "+answer)