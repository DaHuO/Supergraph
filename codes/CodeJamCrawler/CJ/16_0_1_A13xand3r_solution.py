def readandwritefile(file):
	with open(file) as f:
		lines = f.readlines()
		numcases = int(lines[0].rstrip())
		linestowrite = []
		for i in range(1, (numcases+1)):
			linestowrite.append(solve(lines[i].rstrip().split()))
		writeanswer(linestowrite, 'file.out')
		f.close()

def writeanswer(lines, file):
	with open(file, 'w+') as f:
		for i in range(0 ,len(lines)):
			line = lines[i]
			f.write("Case #" + str(i+1) + ": " + line)
			if(i+1 < len(lines)):
				f.write("\n")
		f.close()











def solve(params):
	startnum = int(params[0])
	if(startnum*2 == startnum):
		return "INSOMNIA"
	else:
		curindex = 0
		curnum = startnum
		checked = []
		while(len(checked) < 10):
			curindex = curindex + 1
			curnum = startnum * curindex
			strnum = str(curnum)
			for ints in strnum:
				if ints not in checked:
					checked.append(ints)
		return str(curnum)





readandwritefile('file.in')