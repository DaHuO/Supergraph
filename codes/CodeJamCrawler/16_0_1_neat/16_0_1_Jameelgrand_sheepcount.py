#!/usr/bin/python
from collections import Counter
import sys
input_list=[]
count=1
digits=[]
current_value=0

def get_input(file_path):
	inputfile=open(file_path)
	for x in inputfile.readlines():
		try:
			# print x.strip()
			# print file_path
			input_list.append(int(x.strip()))
		except:
			print "wrong inputfile"
			exit()
def unique_digits(n):
	global digits
	global count
	global current_value
	sync_digits(n)
	if len(digits)==10:
		return str(n)
	else:
		count=count+1
		return unique_digits(current_value*count)
def sync_digits(list1):
	global digits
	list_of_ints = [int(i) for i in str(list1)]
	newdata=list(set(list_of_ints))
	digits = list((Counter(digits)|Counter(newdata)).elements())



if __name__ == '__main__':
	#global digits
	get_input(sys.argv[1])
	T=input_list[0]
	testcases=input_list[1:]
	if (1 <= T) and (T<=100):
		index=1
		
		for testcase in testcases:
			count=1
			digits=[]
			current_value=testcase
			try:
				print "Case #"+str(index)+": "+unique_digits(testcase)
				index=index+1
			except Exception,e:
				print "Case #"+str(index)+": INSOMNIA"
				index=index+1
				
	else:
		print "testcases limit exceeded"