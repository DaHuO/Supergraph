import sys
# The first line of the input gives the number of test cases, T. T test cases follow. 
# Each consists of one line with three integers: K, C, and S
if __name__ == '__main__':
	rb = open(sys.argv[1],'r')
	wb = open(sys.argv[2],'w')
	n = int(rb.readline().strip())
	for i in range(1, n+1):
		no = rb.readline().split()
		k = int(no[0])
		c = int(no[1])
		s = int(no[2])
		sol = 0
		if k == 1 and s == 0 or k > s+1 or c == 1 and k > s:
			wb.write('Case #'+str(i)+': IMPOSSIBLE\n')
			continue
		if k == 1:
			wb.write('Case #'+str(i)+': 1\n')
			continue
		if c == 1:
			wb.write('Case #'+str(i)+':')
			for j in range(1, k+1):
				wb.write(' '+ str(j))
			wb.write('\n')
			continue
		wb.write('Case #'+str(i)+':')
		for j in range(2, k+1):
			wb.write(' '+ str(j))
		wb.write('\n')
	rb.close()
	wb.close()
