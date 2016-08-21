# Bleatrix shit
import sys

input_file = r"C:\Documents and Settings\Dell D610\My Documents\Code\GCJ\Round0\Prob1\input.txt"
output_file = r"C:\Documents and Settings\Dell D610\My Documents\Code\GCJ\Round0\Prob1\output.txt"
output = open( output_file, 'w')
input = list()
use_file = True
if use_file == True:
	file = open( input_file, 'r' )
	input = [int(line.rstrip()) for line in file]
	file.close()
else:
	input = ( 5, 0, 1, 2, 11, 1692 )
digits = ( '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' )

def splitStringIntoChars( string ):
	return list( string )

def countAgain( N, i ):
	count = N*i
	countStr = str( count )
	chars = splitStringIntoChars( countStr )
	return chars

def solveBleatrix( input ):
	num_cases = int( input[0] )
	input = input [1:]
	
	for index_case in range( 0, num_cases ):
		N = input[index_case] # Get the number for this round of counting
		insomnia_count = 10000
		asleep = False # We're gonna do this till she falls asleep`
		these_digits = digits # Get a copy of the digits to tick off
		i = 1 # We start with N*i (i=1)
		while asleep != True:
			chars = countAgain( N, i )
			these_digits = [x for x in these_digits if x not in chars]
			if len( these_digits ) == 0:
				asleep = True
				final_number = N * i
				statement = "Case #%d: %d\n" % ( ( index_case + 1 ), final_number )
				output.write( statement )
			elif i >= insomnia_count:
				asleep = True
				statement = "Case #%d: INSOMNIA\n" % ( index_case + 1 )
				output.write( statement )
			i += 1
	output.close()
solveBleatrix( input )
