def analyse(line):
	n = int(line)
	if n == 0:
		return "INSOMNIA"

	print("Starting " + str(n))
	missing = {str(i) for i  in range(10)}

	value = 0	
	while missing:
		value += n
		#print(value, set(str(value)), missing)
		missing -= set(str(value))
		

	return str(value)

def run(name):
	lines = [l for l in open(name + ".in", mode='r')]
	n = int(lines[0])
	
	out = open(name + ".out",mode='w')
	for i, line in enumerate(lines[1:]):
		answer = analyse(line[:-1])
		out.write("Case #" + str(i+1) + ": " + answer + "\n")
	out.close()

run("A-large")