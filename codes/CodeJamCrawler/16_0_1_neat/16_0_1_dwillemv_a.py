import __future__
import sys

def getTrotNumber(num):
	seen =[False] * 10
	reps=1000
	last="INSOMNIA"
	for i in range(1, reps):
		current=str(int(num)*i)
		#print(current)
		for e in current:
			digit=int(e)
			seen[digit]=True
		seenAll=True
		for e in seen:
			if not e:
				seenAll=False
				break
		if seenAll:
			return current
		if i==reps and not seenAll: return "INSOMNIA"
	return last

f=open(sys.argv[1], "r")
lst=f.readlines()
f.close()
nCases=int(lst[0])
if nCases != len(lst) -1: sys.stderr.write("NCase mismatch.")
for i in range(1, len(lst)):
	case=getTrotNumber(lst[i])
	print("Case #" +str(i) +": " +case)
