import sys


f = open('A-large.in', 'r')
w = open('outputfile', 'w')

T = int(f.readline())
for i in range(1,T+1):
	temp = f.readline()
	newstring = temp[0]
	for j in range(1,len(temp)):
		if temp[j] >= newstring[0]:
			newstring = temp[j] + newstring
		else:
			newstring = newstring + temp[j]






	w.write("Case #" + str(i) + ": " + newstring)
w.close()	
	
	









