import numpy as np
import sys 

def read_case(file_in):
	A = file.readline()
	return A


file = open(sys.argv[1],'r+')
num_entries =  int(file.readline())
print "The Number Of Entries: " + str(num_entries)
#num_entries = 1

result = []


file_out = open('output.out','wr')
for i in range(num_entries):
	unsort = list(read_case(file))[:-1]
	sort = [unsort[0]]
	for j in range(1,len(unsort)):
		if ((unsort[j] > sort[j-1]) and (unsort[j] >= sort[0])):
			sort =  list(unsort[j]) + sort
		else:
			sort = sort + list(unsort[j]) 
	print sort

	index = str(i+1)
	val   = ''.join(sort)
	string = 'Case #%s: %s\n' % (index, val)
	print string
	file_out.write(string)	

file.close()
file_out.close()

