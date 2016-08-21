f = open("input", "r")
o = open("output", "w")
t = int(f.readline())
for x in range(t):
	s = f.readline()[:-1]
	
	word = s[0]
	for each in s[1:]:
		if each >= word[0]:
			word = each + word
		else:
			word = word + each
	print word
	line = word
	o.write("Case #" + str(x+1) + ": " + str(line) + "\n")
o.close()
f.close()
