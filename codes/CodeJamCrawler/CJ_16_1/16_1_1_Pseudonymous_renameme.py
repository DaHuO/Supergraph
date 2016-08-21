inp = open("A-large (1).txt").readlines()[1:]
out = open("A-small-out.txt", "w+")
for i in range(len(inp)):
	inp[i] = inp[i].replace("\n", "")
for x in range(len(inp)):
	i = inp[x]
	s = i[0]
	for let in i[1:]:
		if ord(let) >= ord(s[0]):
			s = let + s
		else:
			s = s + let
	out.write("Case #{}: {}{}".format(x+1,s,"\n"))