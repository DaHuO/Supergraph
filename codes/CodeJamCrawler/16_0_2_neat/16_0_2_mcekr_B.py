
inp = open('B-large.in',"r")
out = open("outB.txt","w")
lines = inp.readlines()
t = int(lines[0])

def reverse(x, i, j):
	x[i:j+1] = reversed(x[i:j+1])
	for i in range(i,j+1):
		if x[i] == "+":
			x[i] = "-"
		else:
			x[i] = "+"

for z in range(1, t + 1):
	s = list(lines[z].strip())
	res = 0

	while not all(x == "+" for x in s):
		if s[0] == "-":
			if "+" in s:
				q = s.index("+")
				reverse(s,0,q-1)
				res += 1
			else:
				reverse(s,0,len(s)-1)
				res += 1
		else:
			q = s.index("-")
			reverse(s,0,q-1)
			res += 1
	fin = ("Case #%i: " + str(res))	% z
	out.write(fin + "\n")	
inp.close()
out.close()	
