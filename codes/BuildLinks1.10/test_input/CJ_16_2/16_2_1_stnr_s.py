import sys
import string

lines=open(sys.argv[1]).readlines()

num=int(lines[0])

i = 1

ltrs = {}

nmbrs=[("ZERO",0), ("EIGHT",8), ("THREE",3), ("FOUR",4), ("TWO",2), ("SIX",6), ("SEVEN",7), ("FIVE",5),  ("NINE",9), ("ONE", 1)]

real = []

for l in lines[1:]:
	for ltr in l:
		if ltr==' ' or ltr=='\n':
			continue
		if (ltrs.has_key(ltr)):
			ltrs[ltr]+=1
		else:
			ltrs[ltr]=1

	for num in nmbrs:
		has = True
		while(True):
			for k in num[0]:
				if (k not in ltrs.keys() or ltrs[k] == 0):
					has=False
					break
			if (has == False):
				break
			for k in num[0]:
				ltrs[k]-=1
			real += [num[1]]

	for ltr in ltrs.keys():
		if ltrs[ltr] != 0:
			print l
	real.sort()
	print "Case #"+str(i) + ": " + string.join([str(x) for x in real], '')
	i+=1
	ltrs={}
	real=[]
			