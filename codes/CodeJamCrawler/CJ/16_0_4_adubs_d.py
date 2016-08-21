import sys

numCases = int(input())

for i in range(numCases):
	params = input().split()
	k = int(params[0])
	c = int(params[1])
	s = int(params[2])
	output = ""
	if k > s+1 or (k == 2 and s == 1):
		output = "IMPOSSIBLE"
	elif k == s:
		output = "1"
		for j in range(1,s):
			output += " " + str(j + 1)
	elif k == s+1:
		if k > 1:
			output = "2"
			for j in range(1,s-1):
				output += " " + str(j + 2)
	print("Case #" + str(i+1) + ": " + output)