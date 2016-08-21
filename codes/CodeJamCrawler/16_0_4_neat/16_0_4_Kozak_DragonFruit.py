count = int(input())
f = open('out.txt', 'w')

for i in range(0,count):
	f.write("Case #" + str(i+1) + ": ")
	inputs = str.split(str(input()))
	tiles = int(inputs[0])
	comp = int(inputs[1])
	students = int(inputs[2])

	if tiles > students and comp == 1:
		f.write("IMPOSSIBLE\n")
	elif tiles == 1:
		f.write("1\n")
	elif comp == 1:
		for x in range(1,tiles+1):
			f.write(str(x) + " ")
		f.write("\n")
	elif comp > 1 and students >= tiles-1:
		for x in range(2,tiles+1):
			f.write(str(x) + " ")
		f.write("\n")

