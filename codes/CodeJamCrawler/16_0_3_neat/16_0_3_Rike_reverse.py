#file = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\inputtest.in", "r")

output = open("C:\\Users\\Rike\\Documents\\GoogleCodeJam\\output.txt", "w")
output.write("Case #1:\n")
N = 16
J = 50
#num_cases = int(file.readline())

import itertools	

def fast_pseudo_prime(n):
	if n % 2 == 0:
		return 2
	if n % 3 == 0:
		return 3
	if n % 5 == 0:
		return 5
	if n % 7 == 0:
		return 7
	if n % 11 == 0:
		return 11
	if n % 13 == 0:
		return 13
	if n % 17 == 0:
		return 17
	if n % 23 == 0:
		return 23
	if n % 29 == 0:
		return 29
	if n % 31 == 0:
		return 31
	if n % 37 == 0:
		return 37
	if n % 41 == 0:
		return 41
	if n % 43 == 0:
		return 43
	return 0

import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

#[i for i in range(1, N - 1)]
#k = set()

found = 0
for m in range(0, N - 2):
	for set in itertools.combinations([i for i in range(1, N - 1)], m):
		for i in range(2, 11):
			sum = 1 + i**(N-1)
			for number in set:
				sum = sum + i**number
			if not fast_pseudo_prime(sum):
				break
		else:
			found = found + 1
			stringi = "1"
			for i in range(1, N-1):
				if i in set:
					stringi = stringi + "1"
				else:
					stringi = stringi + "0"
			stringi = stringi + "1"
			for i in range(2, 11):
				sum = 1 + i**(N-1)
				for number in set:
					sum = sum + i**number
				stringi = stringi + " "+ repr(fast_pseudo_prime(sum))
			output.write(stringi + "\n")
		if found == J:
			break
	if found == J:
			break

'''for i in range(num_cases):
	output.write("Case #" + repr(i + 1) + ": ")
	number = int(file.readline().strip())
	
	
	#print(counter * number)
	output.write(repr(counter * number) + "\n")'''
output.close()
#file.close()