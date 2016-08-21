


filename = "B-large.in"
f = open(filename, "r")
content = [x.strip('\n') for x in f.readlines()]
f.close()

f = open("output_B.out","w+")

for i,x in enumerate(content[1:]):
	count = 0
	for y in range(0,len(content[i+1])-1):
		if content[i+1][y] != content[i+1][y+1]:
			count += 1
	if content[i+1][len(content[i+1]) - 1] == '-':
		count += 1

	f.write("Case #" + str(i+1) + ": " + str(count) +"\n")

f.close()