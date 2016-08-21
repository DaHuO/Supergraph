import time
with open("/Users/danielvebman/Downloads/sleep.in.txt", "r") as input:
	cases = []
	for line in input:
		for n in range(10):
			if str(n) in line and line.rstrip().translate(None, " ").isdigit():
				line = line.rstrip()
				line = line.translate(None, " ")
				line = int(line)
				cases.append(line)
				break
	numOfCases = cases[0]
	cases.pop(0)
	
	increment = 0
	for n in cases:
		if str(n).isdigit():
			increment += 1
			state = "INSOMNIA"
			numbers = []
			i = 1
			c = True
		
			start_time = time.time()
			last = 0
			while(c):
				for q in range(10):
					if str(q) in str(n*i) and q not in numbers:
						numbers.append(q)
						last = n*i
				c = False
				for g in range(10):
					if g not in numbers:
						c = True
				if time.time() - start_time > 5:
					break
				i += 1
			
			if c is False:
				state = last
			with open("/Users/danielvebman/Downloads/sleep.out.txt", "a") as output:
				output.write("Case #"+str(increment)+": "+str(state)+"\n")