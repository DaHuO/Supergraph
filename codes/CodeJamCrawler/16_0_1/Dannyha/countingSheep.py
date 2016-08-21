#!/usr/bin/python3
T = int(input())
for testNum in range(T):
	N = int(input())
	curr = 1
	if N == 0:
		print("Case #%i: INSOMNIA"%(testNum+1))
	else:
		seenNums = {s:False for s in [str(i) for i in range(10)]}
		while True:
			currNum = curr * N
			# print("currNum: %i"%currNum)
			for c in str(currNum):
				seenNums[c] = True
			if not all(seenNums.values()):
				curr += 1
			else:
				print("Case #%i: %i" %(testNum+1,currNum))
				break


