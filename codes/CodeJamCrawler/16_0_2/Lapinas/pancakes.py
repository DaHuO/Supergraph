fin = open('input', 'r')
fout = open('output', 'w')
tests = int(fin.readline())
for i in range(tests):
	s = fin.readline()
	c = ''
	short = ""
	for j in range(len(s)):
		if c != s[j]:
			short = short + s[j]
			c = s[j]
	count = 0
	if i != tests-1:
		short = short[:-1]
	last = len(short) - 1

	for j in range(len(short)):
		if (short[j] == '+') and (j < last):
			count = count + 1
		if short[j] == '-':
			count = count + 1
	fout.write("Case #"+str(i+1)+": "+str(count)+"\n")

fin.close()
fout.close()