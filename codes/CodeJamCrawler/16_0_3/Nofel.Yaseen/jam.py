import sys
import math

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return 2
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return divisor
    return True

def base_power(my_string,base):
	# my_string = str(my_num)
	my_sum = 0
	my_length = len(my_string)
	for x in xrange(0,my_length):
		my_sum = my_sum + int(my_string[x]) * (base**(my_length - x - 1))
	# print my_sum
	return my_sum

def generateJams(jam_length):
	start = [0 for i in range(jam_length)]
	# print start
	# sys.exit()
	start[0] = 1
	start[jam_length-1] = 1
	total = 0
	# all_jams = []
	for i in xrange(0,max_combs(jam_length-2)):
		# print "im here"
		curJam =  "{0:b}".format(i)
		# print "curJam: " ,curJam
		# print "i: ", i
		index = 0
		if len(curJam) < jam_length-2:
			add_length = jam_length-2 - len(curJam)
			curJam = ('0' * add_length) + curJam
		for each_char in curJam:
			# print "im here2"
			index = index+1
			if each_char == '0':
				# print "index: " , index
				# print "each_char is: ", each_char
				start[index] = 0
			else:
				# print "each_char is: ", each_char
				start[index] = 1
		returned_data = check_jam(start[:])
		if returned_data:
			total = total + 1
			temp_string = ''.join(str(e) for e in start[:])
			print temp_string,
			for each_num in returned_data:
				print each_num,
			print "\n",
			if total == j:
				sys.exit()
		# print "start: " , start
		# temp = start
		# all_jams.append(start[:])

	# return all_jams

def max_combs(my_num):
	return 2**my_num

def check_jam(cur_jam):
	cur_jam = ''.join(str(e) for e in cur_jam)
	# my_flag = False
	# print "printing test jam: ", cur_jam
	# sys.exit()
	test_list = []
	for x in xrange(2,11):
		value = isPrime(base_power(cur_jam,x))
		if value == True:
			# flag = False
			return False
		else:
			test_list.append(value)
	return test_list

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n,j = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	print "Case #1:"
	my_jams = generateJams(n)
	


