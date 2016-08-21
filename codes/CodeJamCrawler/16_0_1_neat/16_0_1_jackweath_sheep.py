no = int(input())

final = [True, True, True, True, True, 
 	 	True, True, True, True, True]

for i in range(0, no):
	total = 0
	number = int(input()) # int
	strNum = str(number)
	nums = [False, False, False, False, False, 
 	 	False, False, False, False, False]
	
	insom = False
	while nums != final:
		non_zero = 0

		for digit in strNum:
			if digit != "0":
				non_zero += 1

			nums[int(digit)] = True

		if non_zero == 0:
			print("Case #" + str(i + 1) + ": INSOMNIA")
			insom = True
			break
		else:
			total += 1

		strNum = str(int(number) * (total + 1))

	if not insom:
		caseText = "Case #" + str(i + 1) + ": "
		print(caseText + str(number * total))

