
def calc_output(x,index):
	
	if x == 0:
		return "Case #" + str(index+1) + ": " + "INSOMNIA"
	n = x;
	count = [0] * 10
	while sum(count) != 10:
		
		for i in str(n):
			if count[int(i)] == 0:
				count[int(i)] = 1
		n = n + x

	return "Case #" + str(index+1) + ": " + str(n-x)


filename = "A-large.in"
f = open(filename, "r")
content = [x.strip('\n') for x in f.readlines()]
f.close()

f = open("output.out","w+")

for i,x in enumerate(content[1:]):
	out = calc_output(int(x),i)
	f.write(out + "\n")

f.close()

	
