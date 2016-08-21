#!/usr/bin/python2

input = []
f = open('B-large.in', 'r')
T = int(f.readline().rstrip()) # Number of test cases.
for i in range(T):
	input.append(f.readline().rstrip())
f.close()

dict = {'-': '+', '+': '-'}

def remove_bottom_happy_pancakes(S):
	while S and S[-1] == "+":
		del S[-1]
	return S

def flip_top_seq_happy_pancakes(S):
	for i in range(len(S)):
		if S[i] != "+":
			S_top_seq_happy = S[:i]
			S_remainder = S[i:]
			break
	S = flip(S_top_seq_happy) + S_remainder
	return S

def flip(S):
	S = S[::-1]
	for i in range(len(S)):
		S[i] = dict[S[i]]
	return S	
	
for i in range(len(input)):
	flips = 0
	S = list(input[i])
	while S:
		while S and S[-1] == "+":
			S = remove_bottom_happy_pancakes(S)	
		if not S:
			break
		elif S[0] == "+":
			S = flip_top_seq_happy_pancakes(S)
			flips += 1
		else:
			S = flip(S)
			flips += 1

	print "Case #%s: %s" % (i+1, flips)
