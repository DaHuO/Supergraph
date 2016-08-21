def solve(s):
	if s == "+" or s == "":
		return 0
	first = s[0]
	last = s[-1]
	if (first == "+" and last == "+"):
		if len(s) == 3:
			return 2
		return 1 + solve(s[1:])
	elif (first == "-" and last == "-"):
		tmp = ""
		for i in range(len(s)):
			if(s[i] == "+"):
				tmp += "-"
			else:
				tmp += "+"
		return 1 + solve(tmp[:-1])
	elif (first == "-" and last == "+"):
		tmp = ""
		for i in range(len(s)):
			if(s[i] == "+"):
				tmp += "-"
			else:
				tmp += "+"
		return 1 + solve(tmp[:-2])
	elif (first == "+" and last == "-"):
		if(len(s) == 2):
			return 2
		if(len(s)/2 % 2 == 0):
			return len(s)/2 + solve(s[:-len(s)/2])
		else:
			return len(s)/2 + solve(s[len(s)/2:])
	return 1


def shorten(S):
	s = ""
	curr = "?"
	for c in S:
		if(c != curr):
			curr = c
			s += c
	return s

fin = open("B-large.in")
fout = open("output.txt", "w")

T = int("".join(fin.readline().split()))

for i in range(T):
	stack = "".join(fin.readline().split())
	fout.write("Case #"+str(i+1)+": "+str(solve(shorten(stack)))+"\n")
	print("Case #"+str(i+1)+": "+str(solve(shorten(stack))))