import math

def make_coinjam(mycoinjam):
	ret = list("10000000000000000000000000000001")

	ii = 30
	while ii > 0:
		if mycoinjam % 2 == 1:
			ret[ii] = '1'
		mycoinjam = mycoinjam // 2
		ii = ii - 1

	return "".join(ret)

N = 32
J = 500

powers = [i ** (N - 1) for i in range(0, 11)]

coinjams = []
divisors = []

numbers = [powers[i + 2] + 1 for i in range(0, 9)]

counter = 0

while len(coinjams) < J:
	
	numberBits = list("000000000000000000000000000000")
	bit = 29
	myCounter = counter
	while counter > 0:
		numberBits[bit] = '1' if counter % 2 else '0'
		counter = counter // 2
		bit = bit - 1

	counter = myCounter

	for i in range(0, 9):
		base = i + 2
		numbers[i] = powers[base] + 1

		addition = 0
		for j in range(0, 30):
			addition = addition * base
			addition = addition + 1 if numberBits[j] == '1' else addition

		numbers[i] = numbers[i] + addition * base

	currentDivisors = []
	for i in range(0, 9):
		base = i + 2
		number = numbers[i]

		found = False
		squareroot = int(math.sqrt(number))
		for j in range(2, min(squareroot, 10000)):
			if number % j == 0:
				found = True
				currentDivisors.append(j)
				break

		if not found:
			break

	if len(currentDivisors) == 9:
		divisors.append(currentDivisors)
		coinjams.append(counter)
		#print("YAY " + str(len(coinjams)) + " / " + str(counter))

	counter = counter + 1

print("Case #1:")
for i in range(0, J):
	s = make_coinjam(coinjams[i]) + " "
	for j in range(0, 8):
		s = s + str(divisors[i][j]) + " "
	s = s + str(divisors[i][8])
	print(s)