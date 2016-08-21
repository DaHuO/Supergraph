# BasicInputA.py
import math
import re
import os
import string

t = int(input())
letters = (string.ascii_uppercase)
#print(t)

for loopNum in range(1, t + 1):

 	partidos = int(input())
 	senadoresStr = str(input())
 	senadores = []

 	senadoresStr = senadoresStr.split()

 	for y in senadoresStr:
 		senadores.append(int(y))

 	maxInt = 0
 	started = False
 	n = ""

 	while not(maxInt == 0) or not(started):
 		started = True
 		i = 0

 		maxInt = 0
 		for x in range(0,len(senadores)):
 			if(senadores[x] > maxInt):
 				maxInt = senadores[x]
 				i = x

 		if(maxInt > 0):
 			n = n + " "
 			n = n + letters[i]
 			senadores[i] -= 1


 		maxInt = 0
 		
 		for x in range(0,len(senadores)):
 			if(senadores[x] > maxInt):
 				maxInt = senadores[x]
 				i = x

 		maxSen = 0
 		for x in senadores:
 			maxSen += x

 		hayMayor = False
 		for x in range(0,len(senadores)):
 			t = senadores[x]
 			if(i == x): 
 				t -= 1
 			hayMayor = hayMayor or (((maxSen - 1) /2) < t )

 		if(maxInt > 0 and not(hayMayor)):
 			senadores[i] -= 1
 			n = n + letters[i]
 			#print("entro")
 	
 	#print(str(senadores))
 	print("Case #{}:{}".format(loopNum, n))
 	#print(t)
	#check out .format's specification for more formatting options


# os.system("pause")