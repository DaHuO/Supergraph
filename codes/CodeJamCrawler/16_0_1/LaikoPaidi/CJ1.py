import sys
import os
import re
fin=open("CJ1Data.txt","r")
fout=open("CJ1Out.txt","w")
lines=fin.readlines()
if(len(lines)>0):
	T=lines[0]
i=0
for line in lines:
	if(i==0):
		T=lines[0]
		i=1
	else:
		remaining=["0","1","2","3","4","5","6","7","8","9"]
		if len(line.split()) > 0:
			N=line.split()[0]
			rema = remaining
			for digit in rema:
				if(digit in N):
					remaining = list(filter(lambda x: x!= digit, remaining))
			prev = int(N)
			while(len(remaining)>0):
				next = prev + int(N)
				if(prev == next):
					break
				else:
					rema = remaining
					for digit in rema:
						if(digit in str(next)):
							remaining = list(filter(lambda x: x!= digit, remaining))
					prev = next
			if(len(remaining)>0):
				fout.write("Case #"+str(i)+": INSOMNIA\n")
			else:
				fout.write("Case #"+str(i)+": "+str(prev)+"\n")
			i +=1
		

fout.close()
fin.close()
