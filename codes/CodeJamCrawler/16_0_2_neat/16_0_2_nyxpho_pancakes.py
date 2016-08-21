import sys

if __name__ == "__main__":
	rb = open(sys.argv[1], 'r')
	wb = open(sys.argv[2], 'w')
	n = int(rb.readline().strip())
	for i in range(0,n):
		line = rb.readline().strip()
		flips = 0
		j = 0
		if line[j] == '-':
			while j < len(line) and line[j] == '-':
				j+=1
			flips+=1
		while j < len(line):
			while j < len(line) and line[j] == '+':
				j+=1
			if j < len(line):
				flips+=2
			while j < len(line) and line[j] == '-':
				j+=1
		wb.write("Case #"+str(i+1)+": " + str(flips)+"\n")
	rb.close()
	wb.close()
