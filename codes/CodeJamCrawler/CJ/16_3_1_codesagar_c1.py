import math
inpt = open('input','r')
oupt = open('output','w')

s = int(inpt.readline().rstrip('\n'))
#n = raw_input('')
for z in range(s):
	n = int(inpt.readline().rstrip('\n'))
	x = map(int,inpt.readline().rstrip('\n').split())
	sm = sum(x)
	l=[]
	for i in range(sm):
		p = x.index(max(x))
		l.append(chr(p+65))
		x[p] = x[p]-1
	plan = l
	final = ''
	if sm%2 != 0:
		final += plan[0]+' '
		for i in xrange(1,sm,2):
			final += plan[i]+plan[i+1]+' '
		ou = 'Case #'+str(z+1)+': '+final+'\n'
		oupt.write(ou)
	elif sm%2 ==0:
		for i in xrange(0,sm,2):
			final += plan[i]+plan[i+1]+' '
		ou = 'Case #'+str(z+1)+': '+final+'\n'
		oupt.write(ou)


