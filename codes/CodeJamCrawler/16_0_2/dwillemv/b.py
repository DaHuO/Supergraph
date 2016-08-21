import __future__
import sys

def getFlipCount(pStack):
	pCount=0
	#print pStack
	pancakes=[]
	for e in pStack:
		if e =="+": pancakes.append(True)
		elif e =="-": pancakes.append(False)
		else: continue
	pancakes.reverse()
		#print(pancakes)
	while len(pancakes) >0:
		#print(pancakes)
		top=len(pancakes)
		if pancakes[-1]:
			for i in range(len(pancakes)-1, -1, -1):
				if not pancakes[i]:
					top=i+1
					pCount=pCount+1
					break
		ready=-1
		for i in range(len(pancakes), ):
			if not pancakes[i]:
				ready=i
				break
		if ready ==-1: return str(pCount)
		#print (str(ready) +", " +str(top))
		pancakes=pancakes[ready:top]
		pancakes.reverse()
		for p in range(len(pancakes)): pancakes[p] = not pancakes[p]
		#if pCount > 3: break
		pCount=pCount+1

f=open(sys.argv[1], "r")
lst=f.readlines()
f.close()
nCases=int(lst[0])
if nCases != len(lst) -1: sys.stderr.write("NCase mismatch.")
for i in range(1, len(lst)):
	#print(lst[i])
	case=getFlipCount(lst[i])
	print("Case #" +str(i) +": " +case)
