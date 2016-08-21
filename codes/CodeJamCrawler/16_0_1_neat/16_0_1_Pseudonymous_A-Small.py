def sleep(x):
	x = int(x)
	z = x
	count = 0
	numbers = []
	if x == 0: return "INSOMNIA"
	while(len(numbers)<10):
		y = str(x)
		for i in y:
			if i not in numbers:
				numbers.append(i)
		x+=z
	return str(x-z)

out = open("A-Large-out.txt", "w+")
inp = open("A-Large.txt").read().split("\n")[1:-1]
for i in range(len(inp)):
	out.write("Case #"+str(i+1)+": "+sleep(inp[i])+"\n")