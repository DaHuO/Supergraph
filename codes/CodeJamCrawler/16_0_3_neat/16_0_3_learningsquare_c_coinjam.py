def iscomposite(num):
	remainder = 2 ** (num-1) % num
	if remainder != 1:
		return True
	elif remainder == 1:
		return False

def find_divisor(num):
	for i in range(2, min(num-1, 1000)):
		if num % i == 0:
			return i
	return -1

def solve_case(length, num_jamcoins):
	numstr = str(10 ** (length-1)  + 1)
	jamcoins = []
	divisorlists = []

	while len(jamcoins) < num_jamcoins:
		num_bases = []
		has_smalldiv = True
		for base in range(2, 11):
			num_bases.append(int(numstr, base))

			divisorlist = []
			for num_base in num_bases:
				divisor = find_divisor(num_base)
				if divisor == -1:
					has_smalldiv = False
				divisorlist.append(divisor)
			
		if has_smalldiv:
			jamcoins.append(numstr)
			divisorlists.append(divisorlist)

		numstr = bin(int(numstr, 2) + 2)[2:]

	return jamcoins, divisorlists