import sys, os

def flip(s,i):
	temps = ''
	for n in range(i):
		ch = s[n:n+1]
		if ch == '-':
			nch = '+'
		else:
			nch = '-'
		temps = nch + temps
	return temps + s[i:]

def findflip(s):
# find right most -
# if left most is -, flip and recurse
# if left most is +, flip all left +'s, flip to right most - and recurse
	if not '-' in s:
		return 0
	else:
		if s[0] == '+':
			return findflip(flip(flip(s[:s.rfind('-')+1],s.find('-')),len(s[:s.rfind('-')+1]))) + 2
		else:
			return findflip(flip(s[:s.rfind('-')+1],len(s[:s.rfind('-')+1]))) + 1
		
infile = r'c:\cj2016\largein.txt'

inf = open(infile,'r')
otf = open(r'c:\cj2016\largeout.txt','w')

nocase = int(inf.readline())

for i in range(1,nocase+1):
	s = inf.readline().strip()
	print s
	x = findflip(s)
	print 'end ' + str(i) + '    ' + str(x)
		
	otf.write('Case #' + str(i) + ': ' + str(x) + '\n')

inf.close()
otf.close()


# find right most -
# if left most is -, flip and recurse
# if left most is +, flip all left +'s, flip to right most - and recurse