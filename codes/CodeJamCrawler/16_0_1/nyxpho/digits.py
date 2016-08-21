import sys

if __name__ == "__main__":
	rb = open(sys.argv[1], 'r')
	wb = open(sys.argv[2], 'w')
	n = int(rb.readline().strip())
	for i in range(0,n):
		number = int(rb.readline().strip())
		if number == 0:
			wb.write("Case #"+str(i+1)+": INSOMNIA\n")
			continue
		digit = dict()
		for j in range(0,10):
			digit[j] = 0
		found = 0
		initial = number
		copy = number
		k=1
		while found < 10:
			number = initial * k
			k+=1
			copy = number	
			while number:
				d = number % 10
				if digit[d] == 0:
					found +=1
					digit[d] = 1
				number = number//10

		wb.write("Case #"+str(i+1)+": " + str(copy)+"\n")
	rb.close()
	wb.close()
