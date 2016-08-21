import math
f = open("D-small-attempt5.in")
h = f.read()

h = h.split('\n')
for i in range(int(h[0])):
	print("Case #" + str(i+1) + ": ",end="")
	k = int(h[i+1].split(' ')[0])
	c = int(h[i+1].split(' ')[1])
	s = int(h[i+1].split(' ')[2])
	sln = []
	if k >= 2:
		for n in range(k):
			print(1 + n*(k**c - 1) // (k - 1),end=" ")
	else:
		print(1,end=" ")
	print()



