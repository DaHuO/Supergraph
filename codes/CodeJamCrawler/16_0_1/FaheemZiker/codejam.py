def findResult(n):
	unique_numbers={}
	if n==0:		
		return -1

	for i in xrange(1,9999999):
		res=n*i
		for k in str(res):
			unique_numbers[k]=True
			if len(unique_numbers)>=10:				
				return res
	return -1


input_file = open('A-large.in', 'r')
output_file = open('A-large.out', 'w')

test_cases=int(input_file.readline())
for t in range(0,test_cases):
	n=int(input_file.readline())
	res=findResult(n)
	if res==-1:
		output_file.write("Case #{case}: INSOMNIA".format(case=t+1))		
	else:
		output_file.write("Case #{case}: {res}".format(case=t+1,res=res))

	if t<test_cases-1:
		output_file.write("\n")


	


