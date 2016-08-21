import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
    	if n % i == 0:
    		return i
    return 0

def convert(base, binaryString, bits):
	ret = 0
	for i in range(len(binaryString)):
		ret += (base**i) * int(binaryString[bits - i - 1])

	return ret

def printVals(binaryString):
	binary = int(binaryString)

	list = [0] * 11
	list[0] = list[1] = 1
	for base in range(2, 11):
		print(binary, 'in base', base, 'is', convert(base, binaryString, len(binaryString)), 'in base 10')
		div = is_prime(convert(base, binaryString, len(binaryString)))

		if not div:
			break

		list[base] = div

	if 0 in list:
		return

	print(binaryString, list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10])

t = int(input())

for i in range(t):
	print('Case #', i+1, ':', sep='')

	nums = input().split()
	n = int(nums[0])
	j = int(nums[1])

	start = 2**(n-1) + 1
	end = 2**n

	for val in range(start, end, 2):
		if j == 0:
			break

		binaryString = str(bin(val))[2:]
		binary = int(binaryString)

		list = [0] * 11
		list[0] = list[1] = 1
		for base in range(2, 11):
			div = is_prime(convert(base, binaryString, n))

			if not div:
				break

			list[base] = div

		if 0 in list:
			continue

		j -= 1
		print(binaryString, list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10])