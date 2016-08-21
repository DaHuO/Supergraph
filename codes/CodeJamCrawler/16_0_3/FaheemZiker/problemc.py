def isPrime(n):
    if n==2:
    	return 2
    if n==3:
    	return 3
    
    for i in range(2,min(n,99999)):   # only odd numbers
        if n%i==0:
            return i

    return None

def find_solution(n,j):
	outputs=0
	num="1"
	num=num.ljust(n-1,'0')
	num=num+"1"	
	dnum=int(num,2)
	result=""
	while outputs<j:	
		bnum=bin(dnum)
		cnum=int(bnum.split("b")[1])

		prime_list=[]
		for base in range(2,11):
			res=int(str(cnum),base)
			p=isPrime(res)			
			if p is not None:
				prime_list.append(str(p))
			else:
				prime_list=None
				break
		
		if prime_list is not None:
			outputs+=1
			result=result+str(cnum)+" "+" ".join(prime_list)
			if outputs<j:
				result=result+"\n"
		dnum+=2
	
	return result




input_file = open('C-large.in', 'r')
output_file = open('C-large.out', 'w')

test_cases=int(input_file.readline())
for t in range(0,test_cases):
	string=input_file.readline()

	res=find_solution(int(string.split(" ")[0]),int(string.split(" ")[1]))
	output_file.write("Case #{case}:\n{res}".format(case=t+1,res=res))

	if t<test_cases-1:
		output_file.write("\n")


	


