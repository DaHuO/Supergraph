import re

list = []
for a in range(1000001):
	seen = [False]*10
	for i in range(100):
		x = a*i
		y = x
		while y!=0:
			seen[y%10] = True
			y //=10
		if all(seen):
			list.append((a,True,i,x))
			break
	else:
		list.append((a,False))

f = open("in.in","r")
w = open("output.txt","w")
num = f.readline()
for it in range(0,int(num)):
	
	n, = [int(l) for l in f.readline().split()]
	
	if list[n][1]:
		res = list[n][3]
	else:
		res = 'INSOMNIA'
	
	print("Case #{0}: {1} ".format(it+1,res))
	w.write("Case #{0}: {1}\n".format(it+1,res))
w.close()