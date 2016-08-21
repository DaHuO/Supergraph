import sys
from sets import Set

def Solve(x):
	A = Set()
	if x == 0:
		return "INSOMNIA"
	b = x
	while True:
		for letter in str(b):
			A.add(letter)
		if len(A) == 10:
			return b	
		b += x	


file = open("A-large.in.txt", "r")
a = [int (row) for row in file]

answer = [Solve(x) for x in a[1:]]

for i, ans in enumerate(answer):
	print "Case #" + str(i+1) + ": " + str(ans)
