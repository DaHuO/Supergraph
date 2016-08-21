import sys
t = input()
t = int(t)
for p in range(1,t+1):
	temp = raw_input().split()
	k = int(temp[0])
	c = int(temp[1])
	sys.stdout.write("Case #"+str(p)+": ")
	for i in range(0,k):
		r = 1+i*(k**(c-1));
		sys.stdout.write(str(r)+" ")
	print ""
