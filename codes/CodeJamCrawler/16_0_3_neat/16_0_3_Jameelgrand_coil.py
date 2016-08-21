#!/usr/bin/python
from collections import Counter
import sys
import string
digs = string.digits + string.letters
input_list=[]
random_list=[]

def binerygen(n):
	for i in xrange(1, 2**n-1):
		yield '1{:0{n}b}1'.format(i, n=n)
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))

def print_non_trivals(random):
	
	base_list=[]
	for i in range(2,11):
		try:
			base_list.append(list(factors((int(random,i))))[0])
		except:
			base_list=[]
			break
	if len(base_list) != 0:
		print_string=random
		for baselist_ele in base_list:
			print_string+=" "+str(baselist_ele)
		print print_string
		return True
	else:
		return False

	
def get_input(file_path):
	inputfile=open(file_path)
	for x in inputfile.readlines():
		try:
			input_list.append(x.strip())
		except:
			print "wrong inputfile"
			exit()
def print_coins(data):
	# print data
	global random_list
	inputs=data.split(' ')
	# print inputs
	for i in range(int(inputs[1])):
		# print int(inputs[0])-2
		for random in binerygen(int(inputs[0])-2):
		 	# print random
			if random not in random_list: 
				if print_non_trivals(random):
					random_list.append(random)
					break

if __name__ == '__main__':
	#global digits
	get_input(sys.argv[1])
	T=int(input_list[0])
	testcases=input_list[1:]
	if (1 <= T) and (T<=100):
		index=1
		for testcase in testcases:
			print "Case #"+str(index)+":"
			random_list=[]
			print_coins(testcase)
			index=index+1
			
				
	else:
		print "testcases limit exceeded"