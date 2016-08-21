test_cases = int(input())

for i in range(test_cases):
	string = input()
	l = []
	temp = ""	
	temp1 = ""
	temp2 = ""	
	for j in range(len(string)):
		if j == 0:
			temp = string[0]
		else:
			temp1 = temp + string[j]
			temp2 = string[j] + temp
			if(temp2 >= temp1): 	
				temp = temp2
			else:
				temp = temp1
	print("Case #",(i+1),": ",temp,sep = "")	
