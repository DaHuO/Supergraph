def last(start):
	cl = []
	end = False
	for x in range(10):
		cl.append(False)
	mu = 1
	while True:
		co = 0
		for x in range(10):
			if cl[x]:
				co+=1
			if co == 10:
				end = True
		if end:
			break
		cu = mu*start
		scu = str(cu)
		for x in scu:
			cl[int(x)] = True
		mu += 1
	return scu

infile = open("/root/Desktop/infile.txt")
outfile = open("/root/Desktop/outfile.txt", "w")
line1 = int(infile.readline())
for case in range(line1):
	start = int(infile.readline())
	if start == 0:
		lastnum = 'INSOMNIA'
	else:
		lastnum = last(start)
	casenum = case + 1
	outfile.write("Case #%s:"% casenum+" "+lastnum+"\n")
infile.close()
outfile.close()
