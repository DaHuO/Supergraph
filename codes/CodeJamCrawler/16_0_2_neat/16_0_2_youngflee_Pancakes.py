file = open("../Downloads/B-large.in")
otherFile = open("../Downloads/PancakesOutputLarge.txt", "w")
lines=file.readline()
lineNumber=1
for line in [yeah.replace('\n','') for yeah in file.readlines()]:
	if(all("+"==character for character in list(line))):
		otherFile.write("Case #"+str(lineNumber)+": 0\n")
		lineNumber+=1
		continue
	if(all("-"==character for character in list(line))):
		otherFile.write("Case #"+str(lineNumber)+": 1\n")
		lineNumber+=1
		continue
	number=0
	for count in range(0,len(line)-1):
		if(list(line)[count]!=list(line)[count+1]):
			number+=1
	if(list(line)[-1]=="-"):
		number+=1
	otherFile.write("Case #"+str(lineNumber)+": "+str(number)+"\n")
	lineNumber+=1