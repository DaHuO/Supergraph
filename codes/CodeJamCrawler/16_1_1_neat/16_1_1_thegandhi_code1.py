content = []
with open("/home/rubal/A-large.in") as f:
    content = f.readlines()


test = int(content[0])

for y in range(1,test+1):
	theinput = content[y]
	

	thenewlist = theinput[0] + ""

	i = 1
	j = 1

	while i < len(theinput):
		if (theinput[i] < thenewlist[0]):
			thenewlist = thenewlist + theinput[i]
		else:
			thenewlist = theinput[i] + thenewlist

		i = i + 1


	print "Case #" + str(y) + ": ",
	print thenewlist
