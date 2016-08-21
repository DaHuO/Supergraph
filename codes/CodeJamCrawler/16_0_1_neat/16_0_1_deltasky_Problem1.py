f = open("A-large.in copy 2")
of = open("A-small.out","w")
l = f.readlines()
totalcases = int(l[0])
print totalcases
for i in range(1,len(l)):
	j = 1
	orgnum = int(l[i])
	incrnum = int(l[i])
	n = set()
	if orgnum == 0:
		of.write("Case #" + str(i) + ": INSOMNIA" + '\n')
	else:
		while len(n) < 10:
			incrnum = orgnum * j
			for c in str(incrnum):
				n.add(c)
			j = j + 1
		if i < totalcases:
			newline = "\n"
		else:
			newline = ""
		of.write("Case #" + str(i) + ": "+ str(incrnum) + newline)

