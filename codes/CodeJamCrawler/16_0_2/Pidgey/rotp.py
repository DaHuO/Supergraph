import numpy as np
import sys 

def read_case(file_in):
	A = file.readline()
	A = str(A[:-1])
	return A 


file = open(sys.argv[1],'r+')
num_entries =  int(file.readline())
print "The Number Of Entries: " + str(num_entries)
#num_entries = 5

result = []
for i in range(num_entries):
	stack = list(read_case(file))
	npan  = len(stack)
	print "\nnpan, stack = ",npan, stack

	stacki = -1*np.ones(npan)
	for j in range(npan):
		if stack[j] == '+':
			stacki[j] *= -1

	print stacki
	count = 0
	for j in range(npan-1,-1,-1):
		if stacki[j] == -1.0:
			stacki[:j+1] *= -1.0
			count+=1
	print count, stacki
	if np.mean(stacki) < 1.0:
		print "ERROR"
		sys.exit(0)

	result.append(count)
file.close()

file_out = open('output.out','wr')
for i in range(num_entries):
	index = str(i+1)
	val   = int(result[i])
	string = 'Case #%s: %s\n' % (index, val)
	print string
	file_out.write(string)	
file_out.close()
