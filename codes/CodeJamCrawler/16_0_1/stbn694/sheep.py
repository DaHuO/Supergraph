def allDigits(digits):
	correct = True
	for n in digits:
		if n == False:
			correct = False
			break
	return correct

input_file = open("A-large.in", "r")
output_file = open("A-large.out", "a")
T = int(input_file.readline())

for i in range(T):
	digits = [False] * 10
	number = int(input_file.readline())
	factor = 1

	if number == 0:
		output_file.write("Case #" + repr(i + 1) + ": " + "INSOMNIA" + "\n")
	else:
		while True:
			value = factor * number
			n = value
			while n:
				digit = n % 10
				digits[digit] = True
				n //= 10
			if allDigits(digits):
				break
			else:
				factor += 1
		output_file.write("Case #" + repr(i + 1) + ": " + repr(value) + "\n")

input_file.close()
output_file.close()