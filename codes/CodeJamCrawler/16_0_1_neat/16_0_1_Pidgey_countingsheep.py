import numpy as np
import sys 

def read_case(file_in):
	A = file.readline()
	A = int(A)
	return A 


file = open(sys.argv[1],'r+')
num_entries =  int(file.readline())
print "The Number Of Entries: " + str(num_entries)
#num_entries = 1

result = []

for i in range(num_entries):
	N = read_case(file)
	print "\nN = ", N
	count = 0
	arrtot = np.zeros(10,dtype=bool)
	for j in range(1,1000):
		if arrtot.all() == 0:
			Ni = str(N*j)
			for k in range(len(Ni)):
				arrtot[int(Ni[k])] =  "True"
			count+=1
	print count, arrtot
	if arrtot.all() == 0:
		out = "INSOMNIA"
	else:
		out = str(N*count)
		
	result.append(out)
file.close()

file_out = open('output.out','wr')
for i in range(num_entries):
	index = str(i+1)
	val   = result[i]
	string = 'Case #%s: %s\n' % (index, val)
	print string
	file_out.write(string)	
file_out.close()
		
