file_to_read = open('A-large.in','r')
file_to_write = open('output.txt','w')
content = file_to_read.read().splitlines()
loop = content[0]
for i in range(1,int(loop)+1):
	digits = []
	n = content[i]
	if n == '0':
		file_to_write.write("Case #%s: %s\n" % (str(i),"INSOMNIA"))
		continue
	j = 1
	while True:
		string = (int(n)*j)
		for digit in str(string):
			if not digit in digits:
				digits.append(digit)
		if (len(digits) == 10):
			break;
		else:
			j = j + 1
	file_to_write.write("Case #%s: %s\n" % (str(i),str(string)))

