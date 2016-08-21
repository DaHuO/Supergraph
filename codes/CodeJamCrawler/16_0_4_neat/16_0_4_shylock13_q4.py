from itertools import permutations
t = int( raw_input() )
for i in range( 1, t+1 ):
	inps = raw_input().split(" ")
	k = int(inps[0])
	c = int(inps[1])
	s = int(inps[2])
	#print k
	#print c
	#print s
	if k == 1:
		print 'Case #{}: {}'.format(i, 1)
		continue
	print 'Case #{}:'.format(i), " ".join([ str(i) for i in range(1,k+1) ])
	continue
	jstr = []
	j=0
	while j <  2**k :
		j +=1
		st = "{0:b}".format(j).zfill(k)
		#print st
		stemp = st
		s0 = ''.join(['0' for l in range(len(st))]) 
		if c==1:
			jstr.append(st)
		for p in range(1,c):
			final_str = ""
			for n in range(0,len(stemp)):
				if stemp[n] == '0': 
					final_str += s0
				else:
					final_str += st
			stemp = final_str
			if p == c-1:
				jstr.append( final_str )
				#print final_str
	rem = 0
	dif = 0
	for j in jstr:
		rem = int(j,2) & rem
		dif = int(j,2) | dif
		length = len(j)
	# print "{0:b}".format(rem).zfill(length)
	# print "{0:b}".format(dif).zfill(length)
	ind = "{0:b}".format(dif).zfill(length).find('0')
	if ind != -1:
		print 'Case #{}: {}'.format(i, ind )
		continue
	else:
		masks = []
		for row in permutations("{0:b}".format( 2**( s ) -1).zfill(length)):
			masks.append( "".join(list(row)) )
		#print masks
		#print jstr
		peaceout = False
		for m in masks:
			#print m
			dif = 0
			nope =False
			for j in jstr:
				if ( int(j,2) & int(m,2) ) == int(m,2):
					nope = True
					break
			if nope:
				continue
			polo = []
			for lp in range( 0, len(m) ):
				if m[lp]=='1':
					polo.append(str(lp+1))
			print 'Case #{}:'.format(i), " ".join(polo)
			peaceout = True
			break
		if not peaceout:
			print 'Case #{}: IMPOSSIBLE'.format(i)

	# print 'Case #{}: {}'.format(i, jstr)


# ------

# GG: GG GG: GG GG GG GG

# GL: GG GL: GG GG GG GL
# LG: LG GG: LG GG GG GG

# LL: LL LL: LL LL LL LL

# ------

# GGG: GGG GGG GGG

# GGL: GGG GGG GGL
# GLG: GGG GLG GGG
# GLL: GGG GLL GLL
# LGG: LGG GGG GGG
# LGL: LGL GGG LGL
# LLG: LLG LLG GGG

# LLL: LLL LLL LLL