file = open("../Downloads/A-large.in")
otherFile = open("../Downloads/CountingSheepOutput2.txt", "w")
lines=file.readline()
lineNumber = 1
for line in [int(yeah.replace('\n','')) for yeah in file.readlines()]:
	if(int(line)==0):
		otherFile.write("Case #"+str(lineNumber)+": INSOMNIA\n")
		lineNumber+=1
		continue
	numbers = {'0':0, '1':0, '2':0,
		'3':0, '4':0, '5':0, '6':0,
		'7':0, '8':0, '9':0}
	i=1
	while(any(number<1 for number in numbers.values())):
		for character in list(str(line*i)):
			numbers[character]+=1
		i+=1
	otherFile.write("Case #"+str(lineNumber)+": "+str(line*(i-1))+"\n")
	lineNumber+=1