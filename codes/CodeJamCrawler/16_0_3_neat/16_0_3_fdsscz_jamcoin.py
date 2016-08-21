import math
import itertools

def is_prime(n):
	if n % 2 == 0 and n > 2: 
		return 2
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return i
	return -1

def generateJamcoin(n,j):
	count = 0
	for string in itertools.imap(''.join, itertools.product('01', repeat=n-2)):
		if count >= j:
			return
		temp_string = '1' + string + '1'
		#print temp_string
		temp_list = list()
		is_jam = False;
		for base in range(2,11):
			if not is_jam:
				curr_num = 0
				for i in range(len(temp_string)):
					if int(temp_string[len(temp_string)-i-1]) == 1:
						curr_num +=  int(math.pow(base,i))
				divider = is_prime(curr_num)
				#print curr_num, divider
				if divider == -1:
					is_jam = True
				else:
					temp_list.append(divider)
		if not is_jam:
			message = temp_string*2
			for i in range(len(temp_list)):
				message += " " + str(temp_list[i])
			print message
			count += 1

t = int(raw_input())  
for i in xrange(1, t + 1):
	n, j = [int(s) for s in raw_input().split(" ")]
	print "Case #{}:".format(i)
	generateJamcoin(n/2,j)