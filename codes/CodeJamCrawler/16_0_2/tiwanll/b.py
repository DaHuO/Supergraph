allnums = [int(x) for x in "1234567890"]

def f(s):
	prev = s[0]
	t = 0
	for c in s:
		if c!=prev:
			t+=1
			prev = c
	if s[-1]=="-":
		t += 1
	return t


inputfile = open("B-large.in", "r")
outputfile = open("B.out", "w")
t = int(inputfile.readline().strip())
for case in range(t):
	s = inputfile.readline().strip()
	ans = f(s)
	outputfile.write("Case #%s: %s\n" % (case+1, str(ans)))
	#print(ans)

