import random
from sympy.ntheory.factor_ import pollard_rho
 
def read_file(name):
	with open(name) as file:
		for line in file:
			yield int(line)

def getRandomString(length):
	if length == 1:
		return "1"
	elif length == 2:
		return "11"
	else:
		string = "1"
		for i in range(length-2):
			if random.random() > 0.5:
				string += "1"
			else:
				string += "0"
		string += "1"
	return string

def getBaseI(string, base):
	num = 0
	for char in string:
		num *= base 
		if char == '1':
			num += 1
	return num


def solve():
	numToFind = 500
	found = 0
	num_iters = 0
	stringsSeen = set([])
	while found < numToFind:
		num_iters += 1
		string = getRandomString(32)
		if (string in stringsSeen):
			continue
		else:
			stringsSeen.add(string)
		factors = []
		for j in range(2,11):
			num = getBaseI(string, j)
			factor = pollard_rho(num,max_steps=100)
			if factor is None:
				break
			else:
				factors.append(str(factor))
			
		else:
			print(string + ' ' + ' '.join(factors))
			found += 1
	print('took ' + str(num_iters) + ' iterations')

if __name__ == '__main__':
	solve()
