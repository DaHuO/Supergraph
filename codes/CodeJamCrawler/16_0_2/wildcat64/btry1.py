import numpy as np

def polar_rev(ax):
	for el in range(len(ax)):
		if ax[el]=='+':
			ax[el]='-'
		else:
			ax[el]='+'
	#print ax
	return list(reversed(ax))
			
def flip(patt,k):
	ale = list(patt)
	ale2 = ale[:k]
	ale3 = ale[k:]
	ale4 = polar_rev(ale2)
	ale4.extend(ale3)
	return ale4

def check_all_pos(err2):
	#print "checkall ",err2
	err = list(err2)
	#print "start=",start
	for e in range(len(err)):
		if err[e]!='+':
			return 0
	return 1

def check_all_neg(err2):
	#print "checkall ",err2
	err = list(err2)
	#print "start=",start
	for e in range(len(err)):
		if err[e]!='-':
			return 0
	return 1



def process(patt):
	stat1 = check_all_pos(patt)
	stat2 = check_all_neg(patt)
	if stat1==1:
		return 1
	if stat2==1:
		vx = list(patt)
		u = len(vx)
		app = []
		for j in range(u):
			app.append('+')
		#print "toreturn","".join(app) 
		return "".join(app)
		#return 1
	v1 = list(patt)
	st = patt[0]
	for k in range(1,len(v1)):
		#print v1[k]
		if v1[k]!=st:
			break;
	#print "k=",k
	#if k!=len(v1)-1:
	res1 = flip(patt,k)
	#else:
	#	res1 = flip(patt,k+1)
	return "".join(res1)

inf = open('B-large.in','r')
inl = inf.readlines()
len1 = len(inl)

intotal = inl[0].split()
total = int(intotal[0])
print "total = ", total

itemx = []
for j in range(1,total+1):
	hola = inl[j].split()
	ola = hola[0]
	#print ola
	itemx.append(ola)

print itemx

ofile = open('outp.txt','w')
for lll in range(len(itemx)):
	axe = itemx[lll]
	k=0
	while check_all_pos(axe)!=1:
		#print "\n\n"
		axxx=process(axe)
		k+=1
		if axxx==1:
			break;
		#print axxx, check_all_pos(axxx)
		axe=axxx
	print "Case #",lll+1,":", k
	ofile.write("Case #"+str(lll+1)+": "+str(k)+"\n")