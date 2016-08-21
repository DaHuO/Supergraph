import math

t = int( raw_input() )

def conv( bin_num, base ):

	ret = 0
	
	#print bin_num
	n = len( bin_num )
	
	tmp = 1
	
	for i in range( n-1, -1, -1 ):
		ret += bin_num[i] * tmp
		#print bin_num[i], tmp
		tmp *= base
	
	return ( ret )

def is_prime( x ):

    if x < 2:
        return ( False )

    if x % 2 == 0:
        return ( False )
        
    sqrt_x = int(x**0.5)+1
    
    for i in range( 3, sqrt_x, 2 ):
        if x % i == 0:
            return ( False )
    
    return ( True )
	
for i in range( 0, t ):
	
	#lo = 2**15
	#hi = 2**16-1
	
	n, j = map( int, raw_input().split( " " ) )
	lo = 2**(n-1)
	hi = 2**n-1
	
	#print lo, hi
	
	print "Case #%d:" % ( i+1 )
	
	C = [0]*15
	D = [0]*15
	
	for k in range( lo, hi+1 ):
	
		if k & 1 == 0:
			continue
			
		num = map( int, bin(k)[2:] )
		
		if num[-1] == 0:
			continue
			
		#print "con", conv( num, 3 )
		
		#print bin(k)[2:], len( bin(k)[2:])
		
		found = True
		num = map( int, bin(k)[2:] )

		for z in range( 2, 11 ):
			tmp =  conv( num, z )
			C[z] = tmp
			D[z] = -1
			#print bin( tmp )
			if is_prime( tmp ):
				found = False
				#print "prime"
				break
		
		if found:
			#print "found"
			#print num
			fl = True
			for z in range( 2, 11 ):
				tmp = C[z]
				for m in range( 2, int( C[z] ** 0.5 ) ):
					if C[z] % m == 0:
						D[z] = m
						break
				if D[z] == -1:
					fl = False
					break
			if fl:
				j -= 1
				print "".join( map( str, num ) ),
				for z in range( 2, 11 ):
					print D[z],
				print
				if j == 0:
					break
