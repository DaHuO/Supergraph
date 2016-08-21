from sys import stdout
from sys import stdin


def read_input():
	arr = [];
	#f = open( "D-large.in" )
	f = stdin
	num = int(f.readline().rstrip())
	for line in f:
		line = line.rstrip();
		arr.append(line)
	if( num != len(arr) ):
		print "ERROR IN INPUT! " + str(num) + "," + str(len(arr))
		return []
	return arr
	
def subtr_letter( char_occ, letter, count ):
	let_ind = ord(letter)-65
	char_occ[let_ind] -= count
	
def let_count( char_occ, letter ):
	let_ind = ord(letter)-65
	return char_occ[let_ind]

def count_chars(S,char_occ):
	for i in range(0,26):
		char_occ.append(0)
		letter = chr(i+65)
		char_occ[i] = S.count(letter)
		
def check_zero(char_occ,resarr):
	mycount = let_count( char_occ, 'Z' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(0)
	subtr_letter( char_occ, 'Z', mycount )
	subtr_letter( char_occ, 'E', mycount )
	subtr_letter( char_occ, 'R', mycount )
	subtr_letter( char_occ, 'O', mycount )
	
def check_eight(char_occ,resarr):
	mycount = let_count( char_occ, 'G' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(8)
	subtr_letter( char_occ, 'E', mycount )
	subtr_letter( char_occ, 'I', mycount )
	subtr_letter( char_occ, 'G', mycount )
	subtr_letter( char_occ, 'H', mycount )
	subtr_letter( char_occ, 'T', mycount )
	
def check_six(char_occ,resarr):
	mycount = let_count( char_occ, 'X' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(6)
	subtr_letter( char_occ, 'S', mycount )	
	subtr_letter( char_occ, 'I', mycount )	
	subtr_letter( char_occ, 'X', mycount )	
	
def check_two(char_occ,resarr):
	mycount = let_count( char_occ, 'W' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(2)
	subtr_letter( char_occ, 'T', mycount )
	subtr_letter( char_occ, 'W', mycount )
	subtr_letter( char_occ, 'O', mycount )
	
def check_four(char_occ,resarr):
	mycount = let_count( char_occ, 'U' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(4)
	subtr_letter( char_occ, 'F', mycount )
	subtr_letter( char_occ, 'O', mycount )
	subtr_letter( char_occ, 'U', mycount )	
	subtr_letter( char_occ, 'R', mycount )
	
def check_three(char_occ,resarr):
	mycount = let_count( char_occ, 'H' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(3)
	subtr_letter( char_occ, 'T', mycount )
	subtr_letter( char_occ, 'H', mycount )
	subtr_letter( char_occ, 'R', mycount )	
	subtr_letter( char_occ, 'E', mycount )			
	subtr_letter( char_occ, 'E', mycount )			
	
def check_five(char_occ,resarr):
	mycount = let_count( char_occ, 'F' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(5)
	subtr_letter( char_occ, 'F', mycount )
	subtr_letter( char_occ, 'I', mycount )
	subtr_letter( char_occ, 'V', mycount )	
	subtr_letter( char_occ, 'E', mycount )			

def check_seven(char_occ,resarr):
	mycount = let_count( char_occ, 'V' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(7)
	subtr_letter( char_occ, 'S', mycount )
	subtr_letter( char_occ, 'E', mycount )
	subtr_letter( char_occ, 'V', mycount )	
	subtr_letter( char_occ, 'E', mycount )	
	subtr_letter( char_occ, 'N', mycount )	
	
def check_one(char_occ,resarr):
	mycount = let_count( char_occ, 'O' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(1)
	subtr_letter( char_occ, 'O', mycount )
	subtr_letter( char_occ, 'N', mycount )
	subtr_letter( char_occ, 'E', mycount )	

def check_nine(char_occ,resarr):
	mycount = let_count( char_occ, 'E' )
	if( mycount == 0 ): return
	for i in range(mycount):
		resarr.append(9)
	subtr_letter( char_occ, 'N', mycount )
	subtr_letter( char_occ, 'I', mycount )
	subtr_letter( char_occ, 'N', mycount )	
	subtr_letter( char_occ, 'E', mycount )	
	

def check_case(tup):
	S = tup
	resarr = []
	char_occ = []
	
	count_chars(S,char_occ)
	check_zero(char_occ,resarr)
	check_eight(char_occ,resarr)
	check_six(char_occ,resarr)
	check_two(char_occ,resarr)
	check_four(char_occ,resarr)
	check_three(char_occ,resarr)
	check_five(char_occ,resarr)
	check_seven(char_occ,resarr)
	check_one(char_occ,resarr)
	check_nine(char_occ,resarr)
	
	#print S
	#print ".".join(map(str,char_occ))
	resarr.sort();
	print "".join(map(str,resarr))
	
	return
	

		
	return ""
#------------------------------------------------------------------------------	
input_arr = read_input()
n_cases = len(input_arr)
for i in range(n_cases):
	stdout.write( "Case #" + str(i+1) + ":" )
	stdout.write( " " ) # single line solution
	result = check_case(input_arr[i])
	



