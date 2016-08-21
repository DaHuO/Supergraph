#from intertools import *

def finder(my):
	ans=[]
	while(my.find('Z')!=-1):
		my = my.replace("Z","",1)
		my = my.replace("E","",1)
		my = my.replace("R","",1)
		my = my.replace("O","",1)
		ans.append(0)
	while(my.find('X')!=-1):
		my = my.replace("S","",1)
		my = my.replace("I","",1)
		my = my.replace("X","",1)
		ans.append(6)
	while(my.find('W')!=-1):
		my = my.replace("T","",1)
		my = my.replace("W","",1)
		my = my.replace("O","",1)
		ans.append(2)
	while(my.find('U')!=-1):
		my = my.replace("F","",1)
		my = my.replace("O","",1)
		my = my.replace("U","",1)
		my = my.replace("R","",1)
		ans.append(4)
	while(my.find('S')!=-1):
		my = my.replace("S","",1)
		my = my.replace("E","",1)
		my = my.replace("V","",1)
		my = my.replace("E","",1)
		my = my.replace("N","",1)
		ans.append(7)
	while(my.find('O')!=-1):
		my = my.replace("O","",1)
		my = my.replace("N","",1)
		my = my.replace("E","",1)
		ans.append(1)
	while(my.find('N')!=-1):
		my = my.replace("N","",1)
		my = my.replace("I","",1)
		my = my.replace("N","",1)
		my = my.replace("E","",1)
		ans.append(9)
	while(my.find('V')!=-1):
		my = my.replace("F","",1)
		my = my.replace("I","",1)
		my = my.replace("V","",1)
		my = my.replace("E","",1)
		ans.append(5)
	while(my.find('R')!=-1):
		my = my.replace("T","",1)
		my = my.replace("H","",1)
		my = my.replace("R","",1)
		my = my.replace("E","",1)
		my = my.replace("E","",1)
		ans.append(3)
	while(my.find('H')!=-1):
		my = my.replace("E","",1)
		my = my.replace("I","",1)
		my = my.replace("G","",1)
		my = my.replace("H","",1)
		my = my.replace("T","",1)
		ans.append(8)
	return ans
k=int(input())
for i in range(k):
	m=input()
	op=finder(m)
	op.sort()
	op=''.join(str(X) for X in op)
	print("Case #"+str(i+1)+": "+op)



