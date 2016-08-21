#!/usr/bin/env python

t=int(input(''))
n_list=[]
def result(x):
	x_list=[]
	for y in range(1000001):
		n=(y+1)*x
		for i1 in str(n):
			if i1 not in x_list:
				x_list.append(i1)
				pass
			pass
		if len(x_list) == 10:
			return(n)
			pass
		pass
	return("INSOMNIA")
	pass
for i in range(t):
	n=int(input(''))
	print("Case #{0}: {1}".format(i+1,result(n)))
	pass