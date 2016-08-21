t = int( raw_input() )

p = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]

memo = [0]*27
how = [0]*27
final = [0]*10

def has( n ):

	global memo, how
	how = [0]*27

	for k in range( 0, len(p[n]) ):
		#print p[n][k]
		how[ ord(p[n][k] ) - ord('A') ] += 1
	
	for k in range( 0, 27 ):
		if how[k] > 0:
			if memo[ k ] < how[k]:
				return ( False )

	return ( True )

def er( n ):
	global memo, how
	for i in range( 0, 27 ):
		memo[ i ] -= how[i]

def inc( n ):
	global memo, how
	for i in range( 0, 27 ):
		memo[ i ] += how[i]


l1 = [ 2, 6, 8 ]
l2 = [ 0, 9, 5, 7, 1, 4, 3 ]
found = False
ret = ""

def f( ):

	global memo, found, final, ret
	
	if found == True:
		return

	tmp = 0
	for j in range( 0, len(memo) ):
		if memo[j] == 0:
			tmp += 1
			
	if tmp == len( memo ):
		#print tmp
		#print final
		found = True
		
		ret = ""
		for j in range( 0, 10 ):
			if final[j] > 0:
				ret += chr( ord('0') + j ) * final[j]
				
		return
		
	for i in range( 0, 10 ):
		if has( i ):
			for k in p[i]:
				memo[ ord(k)-ord('A') ] -= 1
			final[i] += 1
			f( )
			for k in p[i]:
				memo[ ord(k)-ord('A') ] += 1
			final[i] -= 1
		
for i in range( 0, t ):
	x = raw_input()
	#print x
	
	memo = [0]*27
	
	for j in range( 0, len(x) ):
		#print x[j],
		memo[ ord( x[j] ) - ord('A') ] += 1	
	
	found = False
	
	final = [0]*10
	#print memo
	
	#for j in l1:
	#	while has( j ) == True:
	#		er( j )
	#		final[j] += 1
			
	f()
			
	print "Case #%d: %s" % ( i+1, ret )
			
	