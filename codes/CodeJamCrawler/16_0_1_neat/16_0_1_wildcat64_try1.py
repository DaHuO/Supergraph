import numpy as np

def striplarge(numx):
	snum = str(numx)
	print "len=",len(snum)
	str2 = snum[:10]
	print str2
	int5 = int(str2)
	print "int5=",int5
	strip(int5)

def strip(numx):
	#print "strip",numx
	axed = []
	if numx<10:
		return [numx]
	while numx>=10:
		p = numx/10
		q = numx%10
		#print p,q
		numx = p
		if q not in axed:
			axed.append(q)
	if p not in axed:
		axed.append(p)	
	return axed

def recursenums(seed):
	nums = []
	k=1
	prevarr = []
	while len(nums)<10:
		arr = strip(seed*k)
		#if arr==prevarr:
			#print seed,'insomnia'
		if seed==0:
			return -1
			#break;
		for el in arr:
			if el not in nums:
				nums.append(el)
		#print "nums=",nums
		last = seed*k
		k+=1
		prevarr = arr
	#print seed, last
	return last

ter = []

innums = np.loadtxt('A-large.in')
tot = int(innums[0])
for x in range(tot):
	ter.append(int(innums[x+1]))

print "ter = ", ter

outf = open('output.txt','w')
for t in range(len(ter)):
	res=recursenums(ter[t])
	if res==-1:
		res = 'INSOMNIA'
	print t, res
	outf.write("Case #"+str(t+1)+":	"+str(res)+"\n")

#print strip(1234567)
#striplarge(123548924346728356847228364872364741)


