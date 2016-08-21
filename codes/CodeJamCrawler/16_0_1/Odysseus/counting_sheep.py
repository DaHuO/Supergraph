#!/usr/bin/python

import sys
import fileinput

def update_list(digit_list, num):
	for i in str(num):
		digit_list[ int(i) ] = True

def check_list(digit_list):
	for i in xrange(10):
		if not digit_list[i]:
			return False
	return True

def count_sheep(initial_number):
	digit_list = [ False for i in xrange(10) ]
	N=1;
	cur_num=initial_number
	while True:
		update_list(digit_list, cur_num)
		if check_list(digit_list) == True:
			return cur_num
		N=N+1
		cur_num=N*initial_number

line_cnt=0
test_cases=1

for line in fileinput.input():
	if(line_cnt > (test_cases)):
		#print 'error'
		break;
	if(line_cnt == 0):
		test_cases=int(line);
	else:
		line=line.split();
		initial_number=int(line[0]);
		if initial_number == 0:
			max_num=0
		else:
			max_num = count_sheep(initial_number)
		if max_num==0:
			print('Case #'+str(line_cnt)+': INSOMNIA')
		else:
			print('Case #'+str(line_cnt)+': '+ str(max_num))
	line_cnt+=1;
