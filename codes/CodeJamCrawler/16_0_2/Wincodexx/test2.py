import fileinput

def flipcount(pancake):
	pans = list(pancake)
	pans.reverse()
	flipcounter = 0
	for i in range(0,len(pans)) :
		if(pans[i] == '-'):
			flip(pans,range(i,len(pans)))
			flipcounter = flipcounter+1

	return flipcounter


def flip(pans,r):
	key = 0
	for i in r :
		if(pans[i] == '-') :
			pans[i] = '+'
		else :
			pans[i] = '-'


res = open("output.txt", 'w')
f = fileinput.input()
T = int(f.readline())
for case in range(1,T+1):
	pancake = f.readline()
	c = flipcount(pancake)
	print str(c)
	res.write("Case #{0}: {1} \n".format(case, str(c)))