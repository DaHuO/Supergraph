t = int( raw_input() )

MINN, MAXN = 200, 1000000
cnt = [0]*10

for i in range( 0, t ):
	n = int( raw_input() )
	#print n
	j = 1
	
	cur = n
	
	tot = 0
	prev = cur
	
	for j in range( 0, 10 ):
		cnt[j] = 0
	
	while True:
	
		tmp = cur
		#print tmp
		while tmp > 0:
			pos =  tmp % 10
			if cnt[ pos ] == 0:
				tot += 1
			cnt[ pos ] = 1
			tmp /= 10
	
		prev = cur
		cur += n
		
		if prev == cur:
			break
		
		if tot == 10:
			break
			
	if tot != 10:
		ret = "INSOMNIA"
	else:
		ret = str( cur-n )
	#print cnt
	print "Case #%d: %s" % ( i+1, ret )
			
			
	