t=int(raw_input())
for _ in xrange(t):
	lis = [0 for i in xrange(26)]
	a = raw_input()
	for i in xrange(len(a)):
		lis[ord(a[i])-65]+=1
	lol = [0 for i in xrange(10)]
	#print lis
	if lis[-1]>0:
		lol[0]+=lis[-1]
		lis[4]-=lis[-1]
		lis[17]-=lis[-1]
		lis[14]-=lis[-1]
		lis[-1]=0
	if lis[6]>0:
		lol[8]+=lis[6]
		lis[4]-=lis[6]
		lis[8]-=lis[6]
		lis[7]-=lis[6]
		lis[19]-=lis[6]
		lis[6]=0
	if lis[22]>0:
		lol[2]+=lis[22]
		lis[19]-=lis[22]
		lis[14]-=lis[22]
		lis[22]=0
	if lis[23]>0:
		lol[6]+=lis[23]
		lis[18]-=lis[23]
		lis[8]-=lis[23]
		lis[23]=0
	if lis[20]>0:
		lol[4]+=lis[20]
		lis[5]-=lis[20]
		lis[14]-=lis[20]
		lis[17]-=lis[20]
		lis[20]=0
	if lis[18]>0:
		lol[7]+=lis[18]
		lis[4]-=lis[18]
		lis[4]-=lis[18]
		lis[21]-=lis[18]
		lis[13]-=lis[18]
		lis[18]=0
	if lis[21]>0:
		lol[5]+=lis[21]
		lis[5]-=lis[21]
		lis[8]-=lis[21]
		lis[4]-=lis[21]
		lis[21]=0
	if lis[17]>0:
		lol[3]+=lis[17]
		lis[19]-=lis[17]
		lis[7]-=lis[17]
		lis[4]-=lis[17]
		lis[4]-=lis[17]
		lis[17]=0
	if lis[14]>0:
		lol[1]+=lis[14]
		lis[13]-=lis[14]
		lis[4]-=lis[14]
		lis[14]=0
	if lis[8]>0:
		lol[9]+=lis[8]
	#print lol
	zz = []
	for i in xrange(len(lol)):
		for j in xrange(lol[i]):
			zz.append(i)
	st = "#"+str(_+1)
	print "Case " + st + ":",
	print ''.join(str(i) for i in zz)
