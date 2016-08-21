import sys

def allDigits(digits):
	return all(digit is True for digit in digits)

def markSeen(valList, digits):
	for val in valList:
		digits[int(val)] = True

with open(sys.argv[1], 'r') as file, open('out', 'w') as out:
	data = file.read().split()

	T = int(data.pop(0))

	for i in range(T):
		N = int(data.pop(0))

		digits = [False for x in range(10)]
		val = N
		
		if val is 0:
			out.write("Case #" + str(i+1) + ": " +  "INSOMNIA" + "\n")
			continue
		
		found = False
		j = 1
		while found is False:
			valAsStr = list(str(val))
			markSeen(valAsStr, digits)

			if allDigits(digits):
				out.write("Case #" + str(i+1) + ": " +  str(val) + "\n")
				found = True
			val = N*j
			j = j + 1

