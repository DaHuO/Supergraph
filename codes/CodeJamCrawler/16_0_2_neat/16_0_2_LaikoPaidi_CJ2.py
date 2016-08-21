import sys
import os
import re

def convertor(x):
	if x == "+":
		return "-"
	else:
		return "+"

fin=open("CJ2Data.txt","r")
fout=open("CJ2Out.txt","w")
lines=fin.readlines()
if(len(lines)>0):
	T=lines[0]
cnt=0
for line in lines:
	if(cnt==0):
		T=lines[0]
		cnt=1
	else:
		stringos=line.split()[0]
		lista=list(stringos)
		moves=0
		while(len(lista)>0):
			while(len(lista)>0 and lista[-1]=="+"):
				lista.pop()
			for i in range(len(lista)):
				if(lista[i]=="-"):
					first=i
					break
			l1=lista[:first]
			l2=lista[first:]
			if(len(l1)>0):
				l1=list(map(convertor, l1))
				moves +=1
			lista=l1+l2
			if(len(lista)>0):
				lista=list(map(convertor, lista))
				moves +=1
		
		fout.write("Case #"+str(cnt)+": "+str(moves)+"\n")
		cnt +=1
		

fout.close()
fin.close()
