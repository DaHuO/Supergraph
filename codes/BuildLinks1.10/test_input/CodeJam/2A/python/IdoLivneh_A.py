import sys
import time
import itertools #use combinations!
import random
import math
import heapq 	#use heapq.heapify(on list); 
				#use heapq.heappop(list) to continuously get the lowest

#in case you need this:
#sys.setrecursionlimit(8000)

def iterate_cases_1lpc(filepath):	#1lpc = 1 line per case
	with file(filepath, 'rb') as f_in:
		for line_index, line in enumerate(f_in):
			if line_index == 0: #T
				continue
			yield line_index, line.strip().split(' ')

def iterate_cases_nlpc(filepath, n):	#nlpc = n line per case
	with file(filepath, 'rb') as f_in:
		case_counter = 1
		case = []
		for line_index, line in enumerate(f_in):
			if line_index == 0: #T
				continue
			case.append(line.strip().split(' '))
			if not line_index % n:
				yield case_counter, case
				case_counter += 1
				case = []

def iterate_cases_subsections(filepath, num_of_subs):		#subsections - with subsections. first line in each gives the lines per subsection.
	with file(filepath, 'rb') as f_in:
		case_counter = 0
		new_case = True
		for line_index, line in enumerate(f_in):
			if line_index == 0: #T
				continue
			if new_case:
				new_case = False
				new_sub_case = True
				sub_cases_left = num_of_subs
				case_counter += 1
				case = []
			if new_sub_case:
				new_sub_case = False
				sub_case = []
				assert len(line.strip().split(' ')) == 1
				lines_left = int(line.strip())
				continue
			if lines_left:
				lines_left -= 1
				sub_case.append(line.strip().split(' '))
			if not lines_left:
				case.append(sub_case)
				sub_cases_left -= 1
				new_sub_case = True
				if not sub_cases_left:
					new_case = True
					yield case_counter, case
					
def iterate_cases_glpc(filepath):		#glpc - given lines per case
	with file(filepath, 'rb') as f_in:
		case_counter = 0
		new_case = True
		for line_index, line in enumerate(f_in):
			if line_index == 0: #T
				continue
			if new_case:
				new_case = False
				case_counter += 1
				case = []
				assert len(line.strip().split(' ')) == 1
				lines_left = int(line.strip())
				if not lines_left:
					new_case = True
					yield case_counter, case
				continue
			if lines_left:
				lines_left -= 1
				case.append(line.strip().split(' '))
			if not lines_left:
				new_case = True
				yield case_counter, case
			
def part_of_list_to_int(array, flags):
	assert len(array) == len(flags)
	output = []
	for index, elem in enumerate(array):
		if flags[index]:
			output.append(int(elem))
		else:
			output.append(elem)
	return output

def list_to_int(array):
	return part_of_list_to_int(array, [True] * len(array))

def part_of_list_to_float(array, flags):
	assert len(array) == len(flags)
	output = []
	for index, elem in enumerate(array):
		if flags[index]:
			output.append(float(elem))
		else:
			output.append(elem)
	return output

def list_to_float(array):
	return part_of_list_to_float(array, [True] * len(array))

def get_max_array_on_index(array, index):
	elem_len = len(array[0])
	assert index < elem_len
	for elem in array:
		assert elem_len == len(elem)
	max_sub = array[0][index]
	max_elem = array[0]
	for elem in array:
		if elem[index] > max_sub:
			max_sub = elem[index]
			max_elem = elem
	return max_elem

def list_index_in_sorted_with_position(a_list, value, pos):
	list_len = len(a_list)
	if list_len == 1:
		if a_list[0] == value:
			return pos
		return -1
	if a_list[list_len/2] > value:
		return list_index_in_sorted_with_position(a_list[:(list_len/2)], value, pos)
	else:
		return list_index_in_sorted_with_position(a_list[(list_len/2):], value, pos + (list_len/2))
	
def list_index_in_sorted_list(a_list, value):
	return list_index_in_sorted_with_position(a_list, value, 0)

def copy_list(list):
	res = []
	res.extend(list)
	return res	

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.
    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

PRIMES_FILENAME = "prime.txt"
def get_primes(N):
	"""First create primes using 'python make_primes.py <N>'
	This will create prime.txt file in the same folder. move it to working folder.
	"""
	primes = []
	with file(PRIMES_FILENAME, 'rb') as f:
		for line in f.readlines():
			p = int(line.strip())
			if p > N:
				break
			primes.append(p)
		else:
			raise ValueError('Create a bigger prime file')
	return primes
			
def choice(a, b):
	"""This is a O(a) runtime a!/(a-b)!b! calc.
	It goes to lengths for keeping the result a small number.
	This assumes a>=b or assertion error will be raised.
	"""
	assert a >= b
	res = 1
	if b > a - b:
		for i in xrange(b + 1, a+1):
			res *= i
		for i in xrange(1, a-b+1):
			res /= i
	else:
		for i in xrange(a-b + 1, a+1):
			res *= i
		for i in xrange(1, b+1):
			res /= i
	return res
	
############################################################
#### add solution here 									####
#### don't forget to change data from str to int/float  ####
############################################################

def my_sort(result):
	if len(result) == 1:
		return result
	if len(result) == 2:
		result.sort()
		return result
	res = []
	a = my_sort(result[:len(result)/2])
	b = my_sort(result[len(result)/2:])
	m = [a, b]
	m.sort()
	res.extend(m[0])
	res.extend(m[1])
	return res

def solve(P, R, S):
	elems = [P, R, S]
	#print elems
	result = []
	if max(elems) - min(elems) >= 2:
		return 'IMPOSSIBLE'
	if elems.count(max(elems)) == 1:
		j = elems.index(max(elems))
		if j == 1:
			i = 0
		else:
			i = j
	elif elems.count(max(elems)) == 2:
		j = elems.index(max(elems) - 1)
		i = (j + 1) % 3
	elif elems.count(max(elems)) == 3:
		i = 0
	
	
	while True:
		#print i, elems
		if elems == [0, 0, 0]:
			break
		if elems[i] == 0:
			i = (i + 1) % 3
			continue
		result.append(i)
		elems[i] -= 1
		i = (i + 1) % 3

	#print result
	result = my_sort(result)
	#print result
				
	real_result = ''
	tran = {0: 'P', 1:'R', 2:'S'}
	for r in result:
		real_result += tran[r]
	
	return real_result
		
def calc_result(case):
	#print case
	result = None
	#print case
	N, R, P, S = list_to_int(case)
	#print N, R, P, S
	result = solve(P, R, S)
	print result
	return result

def main(filepath):
	# if needed, define global primes here and get it from file.
	start_time = time.time()
	with file('output.txt', 'wb') as f_out:
		
		######################################
		#### select input iteration type: ####
		####	- iterate_cases_1lpc	  ####
		####	- iterate_cases_nlpc +n	  ####
		####	- iterate_cases_glpc	  ####
		######################################
		for case_index, case in iterate_cases_1lpc(filepath):
			
			print "case #%d: time:%.02f" % (case_index, time.time() - start_time)
			result = calc_result(case)
			
			#######################
			#### format output ####
			#######################
			f_out.write("Case #%d: %s\n" % (case_index, result))
				
if __name__ == '__main__':
	main(sys.argv[1])
