# BasicInputA.py
import math


t = int(input())

#The algorith may be a little bit weird, but I thought the whole as if it were a tree
#
#
#					  A
#				/	|	|	\
#			B 		C 	D 	E
#				....
#	Node1 Node2 Node3
#

# Taking that into consideration, we can easily trace the origin of each leaft.
# For example, in a (depth 3)  (blocks 4) tree, to get to the leaf number 17 you will need to follow the 2-1-2 path.
# 17 = (2-1) * (4**2) + (1-1) * (4**1) + (2-1) * (4**0)
# 17 = 1 * 16 + 0 * 4 + 1 * 1
#
###################################
# The formula is the following
#
#			d < depth		
# 		Position = 	Sum ( (PathTaken - 1) * (blocks ** d) )
# 			d = 0; d+1 
##################################

def getLeafPos(c,k,pathTakens):
	pos = 0	
	for x in range(0, c):
		pos += (pathTakens[x]) * (k** (x))
	return pos


# We also now that if a Path ends with an L, all the previous parents must have been Lead.
# And thanks to how the structure replicates, if a Path is Lead, there is no chance it never was Lead.
# Therefore, if we check a certain Path and it isn't Gold, we know no part of that Path was gold.
#
# In other words, checking for gold is as easy as getting one arrray of Paths that contains an instance of every initial tile.


for loopNum in range(1, t + 1):
 	k,c,s = (input().split())
 	k = int(k)
 	c = int (c)
 	s = int (s)


 	if(k > s * c):
 		n = ["IMPOSSIBLE"]
 	else:
 		n = []
 		currentPos = 0
 		doneEverything = False
 		while(not(doneEverything)):
 			currentPath = []
 			for x in range(0, c):
 				currentPath.append(currentPos)
 				currentPos += 1
 				if(currentPos == k):
 					currentPos = 0
 					doneEverything = True
 			n.append(getLeafPos(c,k,currentPath) +1)




 	printstring = "Case #{}:".format(loopNum)
 	for x in range(0,len(n)):
 		printstring += " {}".format(n[x])
 	print(printstring)