import numpy as np

def strToVec(s):
	v = [0]*26
	for l in s:
		v[ord(l)-ord('A')] += 1
	return np.array(v)

def vecToStr(v):
	r = []
	for i,c in enumerate(v):
		for j in range(int(c)):
			r.append(i)
	return r

def solve(input):
	v = strToVec(input)
	solved = np.linalg.lstsq(A.T, v)[0]
	solved = [abs(round(x)) for x in solved]

	res = sorted(vecToStr(solved))
	return "".join([repr(x) for x in res])

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

A = []
for d in digits:
	A.append(strToVec(d))
A = np.array(A)

for t in range(int(input())):
	print("Case #{:d}:".format(t+1), solve(input()))