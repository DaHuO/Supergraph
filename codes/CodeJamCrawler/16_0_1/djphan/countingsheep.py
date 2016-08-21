import sys

def countSheep(inputNum):
	if inputNum == 0:
		return 0
	else:
		digits = set()
		number = inputNum

		while True:
			for i in str(number):
				if int(i) not in digits:
					digits.add(int(i))

			if len(digits) == 10:
				break

			number += inputNum

		return number


caseNum = int(input())
counter = 0

while counter < caseNum:
	output = countSheep(int(input()))
	if output == 0:
		print ("Case #" + str(counter+1) + ": INSOMNIA")
	else:
		print ("Case #" + str(counter+1) + ": " + str(output))  

	counter += 1
	


