#!/usr/bin/python
from collections import Counter
import sys
input_list=[]
count=1
cakes=[]
loopcount=0
def get_input(file_path):
	inputfile=open(file_path)
	for x in inputfile.readlines():
		try:
			# print x.strip()
			# print file_path
			input_list.append(x.strip())
		except:
			print "wrong inputfile"
			exit()
def flipping_count(list1):
	global count
	global loopcount
	# print list1
	for i in range(len(list1)):
		if '+' in list1:
			if '-' not in list1:
				return str(count)
			if list1[i]=='+':
				if i == loopcount and '+' not in list1[1:]:
					return str(count+1)
				elif i == loopcount and list1[i+1] == '+':
					# count=count+1
					# return flipping_count(list1[:i]+makerev(list1[i:1]))
					loopcount=loopcount+1
					continue
				elif i == loopcount:
					count=count+1
					loopcount=0
					return flipping_count(list1[:i+1]+makerev(list1[i+1:]))

				else:
					count=count+1
					loopcount=0
					# print "as it is"+str(list1[:i])
					# print "reverse"+str(list1[i:])
					
					return flipping_count(list1[:i]+makerev(list1[i:]))
		else:
			break
	count=count+1
	return str(count)




def makerev(n):
	for i in range(len(n)):
		if n[i]=='-':
			n[i]='+'
		else:
			n[i]='-'
	return n

	



if __name__ == '__main__':
	#global digits
	get_input(sys.argv[1])
	T=int(input_list[0])
	testcases=input_list[1:]
	if (1 <= T) and (T<=100):
		index=1
		
		for testcase in testcases:
			count=0
			loopcount=0
			cakes=list(testcase)[::-1]
			print "Case #"+str(index)+": "+flipping_count(cakes)
			index=index+1
			
				
	else:
		print "testcases limit exceeded"