def someFunction(happy):
	alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	word = happy[0]
	for x in range(1, len(happy)):
		if alph.index(happy[x]) >= alph.index(word[0]):
			word = happy[x] + word
		else:
			word += happy[x]
	return word

f = open('A-large.in', 'r')
g = open('A-large.txt','w')

lines = int(f.readline())
for x in range(1,lines+1):
	happy = list(f.readline().strip("\r\n"))
	last = someFunction(happy)
	g.write("Case #%d: %s\r\n" %(x, last))

f.close()
g.close()