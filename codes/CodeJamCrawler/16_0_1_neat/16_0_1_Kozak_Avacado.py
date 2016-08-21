count = int(input())
f = open('out.txt', 'w')


import os,sys
import subprocess
import glob
from os import path

def isIn (number, compare):
	if number in compare:
		return True
	return False

for i in range(0,count):
	startNum = str(input())
	lst = ["0","1","2",'3','4','5','6','7','8','9']
	x = 0
	isDone = True
	newstr = ""
	while isDone == True:
		x = x + 1	
		new = int(startNum)*x
		newstr = str(new)
		for j in lst:
			remo = isIn(j,newstr)
			if remo == True and j != "-":
				lst[int(j)] = "-"
		if lst == ["-","-","-","-","-","-","-","-","-","-"]:
			isDone = False
		if x > 100:
			isDone = False
			newstr = "INSOMNIA"
	f.write("Case #"+str(i+1)+": "+str(newstr)+"\n")