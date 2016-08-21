import os
import random
import math

def isPrime(n):
	if n == 2:
		return 1
	if n%2 == 0:
		return 0

	for i in range(3, math.ceil(n ** 0.5)):
		if n % i == 0:
			return 0
	return 1

def numBase(number, base):
	length = len(number)
	number = str(number)

	final = 0
	for i in range(0, length):
		final += int(number[i]) * (base ** (length-1-i))
	return final

def findFac(num):
	for i in range(2, num-1):
		if num%i == 0:
			return str(i)

file_path_input = os.getcwd() + '/' + 'prob3.in'
file_path_output = os.getcwd() + '/' + 'prob3.out'

with open(file_path_output, 'wb') as output_data:
	with open(file_path_input, 'rb') as input_data:
			num_cases = int(input_data.readline())

			for i in range(num_cases):
				curr_case = input_data.readline().decode().split()
				N = int(curr_case[0])		# Number of binary digits in number
				J = int(curr_case[1])		# Number of examples required

				output_data.write(('Case #' + str(i+1) + ':\n').encode())

				count = 0
				finArr = ['NULL']*J
				while(count != J):	
					curr_num = '1'
					for j in range(N-2):
						curr_num += str(random.randrange(0,2))
					curr_num += '1'

					if curr_num not in finArr:
						ansArr = [-1]*9
						for j in range(2, 11):
							curr_numBaseJ = numBase(curr_num, j)
							
							if (not isPrime(curr_numBaseJ)):
								ansArr[j-2] = curr_numBaseJ
							else:
								break

						if -1 not in ansArr:
							finArr[count] = curr_num
							count += 1
							
							output_data.write((curr_num + ' ').encode())
							for j in range(0, 9):
								output_data.write((findFac(ansArr[j]) + ' ').encode())

							output_data.write('\n'.encode())
							print('COUNT::  ' + str(count))


	input_data.close()
output_data.close()
