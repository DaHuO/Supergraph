import math

def is_prime(num):
	if num == 2 or num == 3:
		return [True, 0]
	if num < 2 or num % 2 == 0:
		return [False, 2]
	for i in range(5, int(math.sqrt(num))):
		if(num % i == 0):
			return [False, i]
	return [True, 0]

def convert_bases(num, base):
	sum = 0
	for i, dig in enumerate(str(num)):
		sum += int(dig)*pow(base, len(str(num))-i-1)
	return(sum)

low = pow(2, 15)
high = pow(2, 16)

count = 1
bool = True

f2 = open('outputSmall.txt', 'w')
final = 'Case #1:\n'

for i in range(low, high):
	val = int(bin(i)[2:])
	string = ''
	if str(val)[-1] == '1':
		bool = True
		for j in range(2, 11):
			num = convert_bases(val, j)
			if is_prime(num)[0]:
				bool = False
				break
			string += str(is_prime(num)[1])+ ' '
		if bool:
			print(count)
			final += '{} {}\n'.format(val, string[:-1])
			count += 1
			if count == 51:
				break

f2.write(final)