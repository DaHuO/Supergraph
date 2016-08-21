filename = "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\input.txt"
outputfilename= "C:\\Users\\Adarsh\\Documents\\Google codejam\\2016\\output.txt"
file = open(filename)
output = open(outputfilename, 'w')
T=int(file.readline())
for x in range(0,T):
	line=file.readline().strip('\t\n\r').split(' ')
	K=int(line[0])
	C=int(line[1])
	S=int(line[2])
	output.write("Case #"+str(x+1)+":")
	for y in range(1,K+1):
		output.write(" "+str(y))
	output.write("\n")