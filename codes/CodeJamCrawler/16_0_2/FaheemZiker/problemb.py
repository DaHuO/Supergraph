
def reverse_stack(string,index):
	if index==0:
		return string
	return string[0:index][::-1].replace("-","*").replace("+","-").replace("*","+")+string[index:len(string)]


def find_solution(string):
	offset=0
	turns=0
	while offset<len(string):				
		last_char=string[offset]		
		is_complete=True
		for i in range(offset,len(string)):
			char = string[i]
			if char!=last_char and '-' in string:
				string=reverse_stack(string,i)
				turns=turns+1				
				offset=i
				is_complete=False
				break		
		
		if is_complete:
			if string[0]=='-':
				turns=turns+1
			return turns

	return turns




input_file = open('B-large.in', 'r')
output_file = open('B-large.out', 'w')

test_cases=int(input_file.readline())
for t in range(0,test_cases):
	string=input_file.readline()
	
	res=find_solution(string)		
	output_file.write("Case #{case}: {res}".format(case=t+1,res=res))

	if t<test_cases-1:
		output_file.write("\n")


	


