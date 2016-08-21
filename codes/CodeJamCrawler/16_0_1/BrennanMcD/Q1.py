#! /bin/bash/py
f = open("A-small-attempt2.in")

h = f.read()


filterList = [0,1,2,3,4,5,6,7,8,9]
x = lambda y: [i * y for i in range(1,1000)]

for i in range(int(h.split('\n')[0])):
	print("Case #" + str(i+1) + ": ", end='')
	s = x(int(h.split('\n')[i+1]))
	cList = []
	for itera in range(1,1001):
		newList = set([int(item) for sublist in [list(str(y)) for y in s[:itera]] for item in sublist])
		if (sum(newList) == 0 and itera == 1000):
			print("INSOMNIA")
			break;
		if list(newList) == filterList:
			print(s[itera-1])
			break;

			
