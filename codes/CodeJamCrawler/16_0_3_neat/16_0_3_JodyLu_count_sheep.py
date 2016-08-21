import fileinput as FileIn
import sys
import math

def ReadData(File, Data):
	for line in FileIn.input(File):
		line = line.replace( "\n", "" )
		Data.append(line)

def counting_sheep(N):
	digits = []
	count = 1
	while True:

		if len(digits) == 10:
			break
		else:
			tmp = N * count
			if count > 1 and tmp == N:
				return 'INSOMNIA'
			count += 1

		while tmp != 0:
			digit = tmp % 10
			if digit not in digits:
				digits.append(digit)
			tmp /= 10

	return N * (count - 1)

def is_all_smile(cakes):
	times = 0
	for cake in cakes:
		if cake == '+':
			times += 1
	if times == len(cakes):
		return True
	else:
		return False



def maneuver(cakes):
	Result = 0
	times = 0
	counter = 0
	bottom = len(cakes) - 1
	top = 0
	tmp = [cakes[i] for i in range(0, len(cakes))]

	while not is_all_smile(tmp):

		top = 0
		bottom = len(cakes) - 1

		# move "bottom" to the first '-'
		while tmp[bottom] == '+':
			bottom -= 1

		# move "top" to the front of first '-'
		while tmp[top] == '+':
			top += 1
		top -= 1

		#print 'top:', top, 'bottom:', bottom

		# the top is '-'
		if top < 0:
			for idx in range(0, bottom + 1):
				if tmp[idx] == '+':
					tmp[idx] = '-'
				else:
					tmp[idx] = '+'
		# the top is '+'
		else:
			for idx in range(0, top + 1):
				if tmp[idx] == '+':
					tmp[idx] = '-'
				else:
					tmp[idx] = '+'
		counter += 1
		#print tmp

	return counter


def prime_test(N):
	if N > 1:
		for i in range(2, int(math.sqrt(N))):
			if(N % i) == 0:
				return i
		else:
			return 1
	else:
		return 1

def convert_N_to_decimal(N, number):
	Result = 0
	power = 0
	while number != 0:
		digit = number % 10
		Result += digit * (N ** power)
		power += 1
		number /= 10
	return Result


def decimal_to_binary(number):
	Result = 0
	digits = []
	while number != 0:
		digit = number % 2
		digits.append(digit)
		number /= 2

	digits.reverse()
	power = len(digits) - 1


	for i in digits:
		Result += i * (10 ** power)
		power -= 1

	return Result


def jamcoin(N, J):
	smallest = 2 ** (N - 1) + 1
	Result = []
	coin = []
	for i in range(0, 2**(N-2)):
		if len(Result) >= J:
			break
		tmp = decimal_to_binary(smallest + 2 * i)
		two_to_ten = [convert_N_to_decimal(i, tmp) for i in range(2, 11)]
		divisor = [prime_test(num) for num in two_to_ten]
		if 1 not in divisor:
			Result.append(divisor)
			coin.append(tmp)

	return coin, Result









if __name__ == '__main__':
	File_1 = 'A-large.in.txt'
	Data_1 = []
	# problem1
	ReadData(File_1, Data_1)
	#print Data
	#print counting_sheep(96)
	#print len(Data)
	#for idx in range(1, len(Data)):
	#	print "Case #" + str(idx) + ':', counting_sheep(Data[idx])
	#print counting_sheep(6)

	# problem2
	#File_2 = 'test.txt'
	#Data_2 = []
	#ReadData(File_2, Data_2)

	#for idx in range(1, len(Data_2)):
	#	print "Case #" + str(idx) + ':', maneuver(Data_2[idx])

	#tmp = [cakes[i] for i in range(0, len(cakes))]
	#print tmp
	#print maneuver(cakes)

	# problem3
	File_3 = 'test.txt'
	Data_3 = []
	ReadData(File_3, Data_3)
	coin, result = jamcoin(32, 500)
	tmp = ""

	for i in range(0, len(coin)):
		tmp = ''.join(str(e) + ' ' for e in result[i])
		print coin[i], tmp

	"""
	N = 6
	J = 3
	smallest = 2 ** (N - 1) + 1
	Result = []
	for i in range(0, 2**(N-2)):
		if len(Result) >= J:
			break
		tmp = decimal_to_binary(smallest + 2 * i)
		#print tmp
		two_to_ten = [convert_N_to_decimal(i, tmp) for i in range(2, 11)]
		divisor = [prime_test(num) for num in two_to_ten]
		if 1 not in divisor:
			Result.append(divisor)
			#print two_to_ten

	print Result
	"""
	"""
	Result = []
	num = [convert_N_to_decimal(i, 1001) for i in range(2, 11)]
	print num

	for i in num:
		if prime_test(i) != 1:
			Result.append(prime_test(i))
	print Result
	"""
