import math

read_file=open(r'input3','r')
input_file=read_file.readlines()
print(input_file)
cases=int(input_file[0])

output=open(r'output3','w')


# turn('+')
# return '-'
def turn(side):
	if side=="+":
		return "-"
	else:
		return "+"

for case in range(cases):
	#case start from 0
	#print("case:",case+1)
	pancake_combination=input_file[case+1]
	#print(pancake_combination)
	L=[]
	for item in pancake_combination:
		L.append(item)
	# whole list of the pancake
	count=0
	top=L[0]
	for x in range(len(L)-1):
		if L[x]!=top:
			count+=1
			#print("L[x]: {}, top: {},position:{}".format(L[x],top,x))
			top=turn(top)
			# print ("top is {}, count is {},x is {}".format(top,count,x))

	if top=="-":
		count+=1
	c=case+1
	output.write("Case #{}: {}\n".format(c,count))






