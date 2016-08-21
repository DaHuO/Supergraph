import sys
import os
import re
import math
fin=open("CJ3Data.txt","r")
fout=open("CJ3Out.txt","w")
lines=fin.readlines()
if(len(lines)>0):
	T=lines[0]
cnt=0
for line in lines:
	if(cnt==0):
		T=lines[0]
		cnt=1
	elif(len(line.split())>2):
		K=int(line.split()[0])
		C=int(line.split()[1])
		S=int(line.split()[2])
		if(S < (K/C)):
			fout.write("Case #"+str(cnt)+": IMPOSSIBLE\n")
		else:
			fout.write("Case #"+str(cnt)+": ")
			itterator=0
			while(itterator<K):
				inner=0
				position = 0
				while(inner<C):
					
					if((inner+itterator)>=K):
						itterator = K
						break
					position += (inner+itterator)*(K**(C-inner-1))
					inner +=1
					#print(position)
                                        
				fout.write(str(int(position)+1)+" ")
				itterator += inner 
			fout.write("\n")
		cnt+=1
			
				
		

fout.close()
fin.close()
