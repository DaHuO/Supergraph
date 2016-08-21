file = open("/Users/daviddai/Desktop/in.txt", "r")
data = file.read()
file.close()

data = data.split()[1:]
opt = ''

for i, j in enumerate(data):
	q = ''
	k = 0
	for ltr in j:
		if k == 0:
			q += ltr
		else:	
			if ord(ltr) >= ord(q[0]):
				q = ltr + q
			else:
				q += ltr
		k = 1
	opt += "Case #" + str(i + 1) + ": " + q + '\n'


file = open('result.txt', 'w')
file.write(opt)
file.close()




