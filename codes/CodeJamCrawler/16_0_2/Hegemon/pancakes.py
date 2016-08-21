filename = "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\input.txt"
outputfilename= "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\output.txt"
file = open(filename)
output = open(outputfilename, 'w')
T=int(file.readline())
for x in range(0,T):
	S=file.readline()
	S = S.strip(' \t\n\r')
	count=0
	for y in range(len(S)):
		if y==(len(S)-1):
			if S[y]=="+":
				output.write("Case #"+str(x+1)+": "+str(count)+"\n")
			else:
				count=count+1
				output.write("Case #"+str(x+1)+": "+str(count)+"\n")
		else:
			if S[y]==S[y+1]:
				continue
			else:
				count=count+1
