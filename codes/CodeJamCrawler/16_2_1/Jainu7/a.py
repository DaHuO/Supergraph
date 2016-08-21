#from intertools import *

t=int(input())
for i in range(t):
	ip=input()
	output=[]
	while(ip.find('Z')!=-1):
		ip = ip.replace("Z","",1)
		ip = ip.replace("E","",1)
		ip = ip.replace("R","",1)
		ip = ip.replace("O","",1)
		output.append(0)
	while(ip.find('X')!=-1):
		ip = ip.replace("S","",1)
		ip = ip.replace("I","",1)
		ip = ip.replace("X","",1)
		output.append(6)
	while(ip.find('W')!=-1):
		ip = ip.replace("T","",1)
		ip = ip.replace("W","",1)
		ip = ip.replace("O","",1)
		output.append(2)
	while(ip.find('U')!=-1):
		ip = ip.replace("F","",1)
		ip = ip.replace("O","",1)
		ip = ip.replace("U","",1)
		ip = ip.replace("R","",1)
		output.append(4)
	while(ip.find('S')!=-1):
		ip = ip.replace("S","",1)
		ip = ip.replace("E","",1)
		ip = ip.replace("V","",1)
		ip = ip.replace("E","",1)
		ip = ip.replace("N","",1)
		output.append(7)
	while(ip.find('O')!=-1):
		ip = ip.replace("O","",1)
		ip = ip.replace("N","",1)
		ip = ip.replace("E","",1)
		output.append(1)
	while(ip.find('N')!=-1):
		ip = ip.replace("N","",1)
		ip = ip.replace("I","",1)
		ip = ip.replace("N","",1)
		ip = ip.replace("E","",1)
		output.append(9)
	while(ip.find('V')!=-1):
		ip = ip.replace("F","",1)
		ip = ip.replace("I","",1)
		ip = ip.replace("V","",1)
		ip = ip.replace("E","",1)
		output.append(5)
	while(ip.find('R')!=-1):
		ip = ip.replace("T","",1)
		ip = ip.replace("H","",1)
		ip = ip.replace("R","",1)
		ip = ip.replace("E","",1)
		ip = ip.replace("E","",1)
		output.append(3)
	while(ip.find('H')!=-1):
		ip = ip.replace("E","",1)
		ip = ip.replace("I","",1)
		ip = ip.replace("G","",1)
		ip = ip.replace("H","",1)
		ip = ip.replace("T","",1)
		output.append(8)
	output.sort()
	output=''.join(str(X) for X in output)
	print("Case #"+str(i+1)+": "+output)



