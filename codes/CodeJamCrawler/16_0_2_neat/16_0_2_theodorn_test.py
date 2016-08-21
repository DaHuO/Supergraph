from sys import stdout

def read_input():
	arr = [];
	f = open( "B-large.in" )
	num = int(f.readline().rstrip( "\n" ).rstrip( "\r" ))
	for line in f:
		line = line.rstrip( "\n" ).rstrip("\r");
		arr.append(line)
	if( num != len(arr) ):
		print "ERROR IN INPUT! " + str(num) + "," + str(len(arr))
		return []
	return arr

def print_current(WS):
	return
	print str(WS[1]).rjust(4) + " " + WS[0]
	
def check_right(WS):
	n_correct = 0;
	for char in reversed(WS[0]):
		if( char == '-' ): break
		n_correct += 1
	if( n_correct == 0 ): return False
	#print "     correct:" + str(n_correct)
	WS[0] = WS[0][:-n_correct]
	print_current(WS)
	return True
	
def check_left(WS):
	needflip = 0;
	for char in (WS[0]):
		if( char == '-' ): break
		needflip += 1
	if( needflip == 0 ): return False
	first_n = WS[0][:needflip]
	first_n = first_n[::-1]
	first_n = first_n.replace( "-", "x");
	first_n = first_n.replace( "+", "-");
	first_n = first_n.replace( "x", "+");
	WS[0] = first_n + WS[0][needflip:]
	WS[1] += 1
	#print "     flip:" + str(needflip)
	print_current(WS)
	return True
	
def flip_all(WS):
	if( len(WS[0]) == 0 ): return False
	flipped = WS[0][::-1]
	flipped = flipped.replace( "-", "x");
	flipped = flipped.replace( "+", "-");
	flipped = flipped.replace( "x", "+");
	WS[0] = flipped
	WS[1] += 1
	#print "     flipall"
	print_current(WS)
	return True	
	
def check_case(S):
	WS = [S,0]; # WS[0] - working string, WS[1] - flips so far
	print_current(WS)
	while( len(WS[0]) > 0 ):
		check_right(WS)
		check_left(WS)
		flip_all(WS)
	return str(WS[1]);

input_arr = read_input()
n_cases = len(input_arr)
for i in range(n_cases):
	result = check_case(input_arr[i])
	print "Case #" + str(i+1) + ": " + result

