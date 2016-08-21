def find_solution(string):
	
	words=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	ordered_chars=["Z","W","U","X","O","G","R","F","V","N"]
	ordered=[0,2,4,6,1,8,3,5,7,9]

	list_chars=list(string)

	output=[]

	while len(list_chars)>0:		
		for ochar in ordered_chars:			
			if ochar in list_chars:

				oindex=ordered_chars.index(ochar)							
				
				word_to_remove=words[ordered[oindex]]				
				output.append(str(words.index(word_to_remove)))								

				for nchar in word_to_remove:				
					dindex=list_chars.index(nchar)
					list_chars.pop(dindex)
				break	
	
	return ''.join(sorted(output))


input_file = open('A-large.in', 'r')
output_file = open('A-large.out', 'w')

test_cases=int(input_file.readline())
for t in range(0,test_cases):
	
	string = input_file.readline().strip()
	res=find_solution(string)	

	output_file.write("Case #{case}: {res}".format(case=t+1,res=res))

	if t<test_cases-1:
		output_file.write("\n")


	


