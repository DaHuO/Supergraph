count = int(input())
f = open('out.txt', 'w')

for i in range(0,count):
	stack = str(input())
	count = len(stack)
	flips = 0
	cnf = stack[0]
	for j in range(0,count):
		if stack[j] != cnf:
			cnf = stack[j]
			flips = flips + 1

	if stack[count-1] == "-":
		flips = flips + 1
	f.write("Case #"+str(i+1)+": "+str(flips)+"\n")

