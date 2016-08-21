import sys
t = int(raw_input())
for i in range(1, t+1):
	flips = 0
	clock = 0
	stack = list(raw_input())
	holding = stack[0]
	for n in stack:
		if n != holding: 
			flips += 1
		holding = stack[clock]
		clock += 1
	if stack[-1] == "-": flips += 1
	print("Case #{}: {}".format(i, flips))
