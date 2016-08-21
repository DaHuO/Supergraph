def switch(a, n):
	d = ""
	for x in reversed(a[:n]):
		d += x		
	d2 = ""
	for l in d:
		if l=="+":
			d2 += "-"
		else:
			d2 += "+"
	for q in a[n:]:
		d2 += q
	return d2
	

with open("/Users/danielvebman/Downloads/pancake.in.txt", "r") as input:
	cases = []
	for line in input:
		if "+" in line.rstrip() or "-" in line.rstrip():
			cases.append(line.rstrip())
	stackNum = 0
	for stack in cases:
		stackNum += 1
		switches = 0
		
		while "-" in stack:
			init = stack[0]
			n = 0
			c = True
			for p in stack:
				if c:
					if p is init:
						n += 1
					else:
						c = False
			stack = switch(stack, n)
			switches += 1
				
		
		with open("/Users/danielvebman/Downloads/pancake.out.txt", "a") as output:
			output.write("Case #"+str(stackNum)+": " + str(switches) + "\n")
		
		"""
		init = "|"
		while("-" in stack):
			n = 0
			for c in stack:
				if init=="|":
					init = c
					n+=1
				elif c is init:
					n+=1
				else:
					break
			switch(stack, n)
			switches += 1
		"""