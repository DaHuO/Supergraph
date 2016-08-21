# Rank and file

# Return an array of collections of ranks (3d)
def extractRanksFromInput( file_path ):
	file = open( file_path )
	num_cases = int( file.readline() )
	collections_of_ranks = list()
	
	while num_cases > len( collections_of_ranks ): # While we have not yet extracted all of the ranks:
		rank_collection_size = int( file.readline() )
		rank_collection = list()
		for index in range( 0, ( rank_collection_size * 2 ) - 1 ):
			rank_collection.append( [int(x) for x in file.readline().rstrip().split()] )
		collections_of_ranks.append( rank_collection )
		
	return collections_of_ranks

def solveRankAndFile( ranks ): # Ranks is an array of integers representing the rows or columns of the grid
	# Find all of the numbers which are represented an odd number of times
	dict = {}
	for rank in ranks:
		for soldier in rank:
			if soldier in dict:
				dict[soldier] += 1
			else:
				dict[soldier] = 1
	
	odd_members = list()
	
	for key in dict:
		if dict[key] % 2 != 0:
			odd_members.append( key )
	
	return sorted( odd_members ) 
	
def main():
	solveRankAndFile( ((1,2,3), (2,3,5), (3,5,6), (2,3,4), (1,2,3)) )
	
if __name__ == '__main__':
	input_file = r"N:\Python Scripts\Round1\Prob1\input.txt"
	output_file = r"N:\Python Scripts\Round1\Prob1\output.txt"
	output = open( output_file, 'w' )

	input = extractRanksFromInput( input_file )
	for case_index in range( 0, len( input ) ):
		solution = solveRankAndFile( input[case_index] )
		output.write( "Case #%d: " % ( case_index + 1 ) )
		for x in solution:
			output.write( "%d " % x )
		output.write( "\n" )