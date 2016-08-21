import numpy as np

tt = int(raw_input(""))

s = 0
npt = 0
partys = []

def delete(index):
	global s
	global npt
	global partys
	
	partys[index]-=1
	s-=1
	if partys[index]==0:
		npt-=1
		
	return chr(ord('A')+index)

for t in range(tt):
	p = int(raw_input(""))
	npt = p
	partys = raw_input("").split(" ")
	
	s = 0
	for i in range(p):
		partys[i] = int(partys[i])
		s+=partys[i]

	res =  "Case #" + str(t+1) + ":"
	partys = np.array(partys)
	while s>0:
		index = np.argmax(partys)
		c1 = delete(index)
		
		c2 = ""
		index = np.argmax(partys)
		
		
		if not (partys[index]==1 and npt==2):
			c2 = delete(index)
			
		res += " "+c1+c2
		
	print res
		
