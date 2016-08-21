import sys

filename=sys.argv[1]

def reverse(stakes):
	res=''
	for stake in stakes:
		if stake=='-':
			res+='+'
		else:
			res+='-'
	return res

def flip(stakes):
	i=0
	while True:
		point = stakes.rfind('-')
		if point<0:
			break
		stakes=reverse(stakes[:point+1])+stakes[point+1:]
		i+=1
	return i

f = open(filename,'rt')
cnt = f.readline()
i=0
for l in f.readlines():
	i+=1
	print 'Case #'+str(i)+':',
	print flip(l.strip())