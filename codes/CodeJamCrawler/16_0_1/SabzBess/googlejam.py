""" 	
Output 
 
5
0
1
2
11
1692

Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076

"""
def readint(): 
	return (raw_input())
file_object = open("A-large.txt", "r")
text_file = open("Output.txt", "w")
line = []
line =file_object.readlines()

linenum = 0
N= int(line[linenum])
linenum+=1
output = "Case #"
finalout = ""
nums = ["1","2","3","4","5","6","7","8","9","0"]
current = []
summ = ""
thing = True
casenum = 1
for i in range(N):
	case = int(int(line[linenum]))
	linenum +=1
	current = []
	nums = ["1","2","3","4","5","6","7","8","9","0"]
	if case == 0:
		output += str(casenum) + ": INSOMNIA"
		thing = False
		
		text_file.write(output+"\n")
		
		casenum +=1
	else:
		thing = True
		
	summ = case
	summ = str(summ)
	for dig in summ:
			current.append(dig)
			
	

	
	
	output = "Case #"
	while len(nums)!= 0 and case != 0:
		same = set(nums).intersection(current)
		same = list(same)
		for l in range(len(same)): #removes
			if same[l] in nums:
				nums.remove(same[l])
		
		summ = int(summ)
		summ += case
		current = []
		summ = str(summ)
		for dig in summ:
			current.append(dig)
		casenum = int(casenum)
	
	if thing:

		
		output += str(casenum) + ": "
		output+= str(int(summ)-case)
		text_file.write(output+"\n")

		casenum +=1
	
			
	


text_file.close()
		