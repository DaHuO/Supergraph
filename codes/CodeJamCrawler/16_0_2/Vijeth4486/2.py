import re
test_cases = int(input())

for i in range(test_cases):
	string = input()
	if('-' not in string):
		print("Case #",(i+1),": ",0,sep = "")
	elif ('+' not in string):
		print("Case #",(i+1),": ",1,sep = "")
	else:
		temp = re.sub('\++','+',string)
		temp = re.sub('\-+','-',temp)
		if(temp[0] == "+" and temp[len(temp)-1] == "+"):
			print("Case #",(i+1),": ",(len(temp) - 1),sep = "")	
		elif(temp[0] == "+" and temp[len(temp)-1] == "-"):
			print("Case #",(i+1),": ",len(temp),sep = "")
		elif(temp[0] == "-" and temp[len(temp)-1] == "-"):
			print("Case #",(i+1),": ",len(temp),sep = "")
		else:
			print("Case #",(i+1),": ",(len(temp)-1),sep = "")
