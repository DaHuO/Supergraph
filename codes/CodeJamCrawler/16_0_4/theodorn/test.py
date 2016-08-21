from sys import stdout

def read_input():
	arr = [];
	f = open( "D-small-attempt0.in" )
	num = int(f.readline().rstrip( "\n" ).rstrip( "\r" ))
	for line in f:
		line = line.rstrip( "\n" ).rstrip("\r");
		arr.append(line)
	if( num != len(arr) ):
		print "ERROR IN INPUT! " + str(num) + "," + str(len(arr))
		return []
	return arr

def check_case(tup):
	temp = tup.split()
	K = int(temp[0])
	C = int(temp[1])
	S = int(temp[2])
	
	#stdout.write( "(" + ",".join([str(K),str(C),str(S)]) + "): " );
	if( C == 1 ): # special case, no additional information can be extracted
		if( S < K ):
			print "IMPOSSIBLE"
			return
		for i in range(1,K): stdout.write( str(i) + " " )
		print str(K)
		return
	
	# additional information available
	if( S < (K+1)/2 ):
		print "IMPOSSIBLE"
		return
	
	all_tiles = K**C
	tiles = []
	for i in range(0,K/2):
		tilenum = all_tiles - i*K - K + i + 1
		tiles.append(str(tilenum))
	if( K & 1 ):
		tiles.append(str(all_tiles/2+1))
	print " ".join(tiles)
		
	return ""
	
input_arr = read_input()
n_cases = len(input_arr)
for i in range(n_cases):
	stdout.write( "Case #" + str(i+1) + ":" )
	stdout.write( " " ) # single line solution
	result = check_case(input_arr[i])
	



