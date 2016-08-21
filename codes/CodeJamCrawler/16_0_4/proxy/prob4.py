infile = open("input4", "r")
outfile = open("output4", "w")

lines = infile.readlines()
T = int(lines[0])

for i,line in enumerate(lines[1:]):
	K,C,S = map(int, line.split())
	
	outfile.write("Case #" + str(i+1) + ":")
	for j in range(1, S+1):
		outfile.write(" " + str(j))
	outfile.write("\n")
