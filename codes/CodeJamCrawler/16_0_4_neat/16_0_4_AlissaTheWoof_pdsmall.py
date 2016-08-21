out = open('./pdout.txt', 'w+')

t = int(input())
for x in range(0, t):
	out.write("Case #" + str(x+1) + ":")
	get = raw_input().split()
	k = int(get[0])
	c = int(get[1])
	s = int(get[2])
	for a in range(1, k+1):
		out.write(" " + str(a))
	out.write("\n")