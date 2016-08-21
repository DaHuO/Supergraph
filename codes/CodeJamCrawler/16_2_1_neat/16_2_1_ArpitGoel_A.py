DIGITS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def checkDigit(listString, digit):
	flag = True
	for d in digit:
		if d in listString:
			listString.remove(d)
		else:
			flag = False
			break

	return flag

def removeString(tempList, digit):
	for d in digit:
		if d in tempList:
			tempList.remove(d)
	return tempList

def checkString(temp, nums):
	
	if len(temp) == 0 and len(nums) > 0:
		return True
	elif len(temp) < 3:
		return False
	else:
		for digit in DIGITS:
			if checkDigit(temp[:], digit) == True:
				nums.append(DIGITS.index(digit))
				temp = removeString(temp[:], digit)
				status = checkString(temp[:], nums)
				if status == True:
					return True
				else:
					temp.extend(DIGITS[nums.pop()])

		return False



f = open('input', 'r')
g = open('output', 'a')
T = int(f.readline())
for i in range(T):
	S = f.readline().strip("\n")
	temp = list(S)
	nums = []
	checkString(temp, nums)
	print(nums)
	nums.sort()
	g.write("Case #{0}: {1}\n".format(i+1, "".join([str(x) for x in nums])))