test_cases = int(input())
output = set({})
no = {0,1,2,3,4,5,6,7,8,9}

def find_no(n):
	temp = set({})	
	while (not(n == 0)):
		temp.add(n%10)	
		n = n // 10
	
	return temp
	  
for i in range(test_cases):
	j = 2
	no = int(input())
	output = find_no(no)
	if(no == 0):
		print("Case #",(i+1),": ","INSOMNIA",sep = "")
	else:
		while(len(output)!=10):
			 output = (output | (find_no(no*j)))
			 if(len(output) == 10):
			 	print("Case #",(i+1),": ",(no*j),sep = "")
			 j = j + 1
			
