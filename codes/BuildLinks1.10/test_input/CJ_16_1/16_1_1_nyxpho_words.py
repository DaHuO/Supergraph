import sys
if __name__ == '__main__':
	rb = open(sys.argv[1],'r')
	wb = open(sys.argv[2],'w')
	n = int(rb.readline().strip())
	for i in range(1, n+1):
		word = rb.readline().strip()
		neww = word[0]
		for l in word[1:]:
			if l < neww[0]:
				neww = neww+l
			else:
				neww = l + neww
		wb.write('Case #'+str(i)+': ' + neww)
		wb.write('\n')
	rb.close()
	wb.close()
