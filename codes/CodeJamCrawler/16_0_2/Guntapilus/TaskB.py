import re

f = open("in.in","r")
w = open("output.txt","w")
num = f.readline()
for it in range(0,int(num)):
	s = f.readline().split()
	l = [c=='+' for c in list(s[0])]
	res = 0
	for i in range(len(l)-1,-1,-1):
		if not l[i]:
			for j in range(0,i+1):
				if not l[j]:
					if j!=0:
						l = [not c for c in l[j-1::-1]]+l[j:]
						res += 1
					break
			l = [not c for c in l[i::-1]]+l[i+1:]
			res += 1
	print("Case #{0}: {1} ".format(it+1,res))
	w.write("Case #{0}: {1}\n".format(it+1,res))
w.close()