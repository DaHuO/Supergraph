import itertools
import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return 2
    x = int(math.sqrt(n)) + 1
    for i in itertools.count(3, 2):
    	# print "NUMBER: " + str(n) + " Squared: " + str(x) + " Squareofsquare: " + str(int(math.sqrt(int(math.sqrt(x))+1))+1) + " iteration: " + str(i)
    	if i > int(math.sqrt(int(math.sqrt(x))+1))+1:
    		break
    	else:
	        if n % i == 0:
	            return i
    return -1

with open("C-large.in") as f:
	content = f.readlines()

T = int(content[0])
Partial = content[1].split()
N = int(Partial[0])
J = int(Partial[1])

array = []
fs = open("output.txt", 'wb')
fs.write("Case #1:\n")
bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
divisors = []

for string in itertools.imap(''.join, itertools.product('01', repeat=(N-2))):
	string = "1" + string + "1"
	check = 0
	divisors = []
	for base in bases:
		power = N-1
		sumin = 0
		for i in xrange(0,len(string)):
			sumin += int(string[i]) * (pow(base, power))
			power = power - 1

		divisor = is_prime(sumin)
		if divisor != -1:
			divisors.append(divisor)
		else:
			check = 1
			break

	if check == 0:
		count += 1
		print count
		fs.write(string + " ")
		for div in divisors:
			fs.write(str(div) + " ")
		fs.write("\n")


	if count == J:
		break

